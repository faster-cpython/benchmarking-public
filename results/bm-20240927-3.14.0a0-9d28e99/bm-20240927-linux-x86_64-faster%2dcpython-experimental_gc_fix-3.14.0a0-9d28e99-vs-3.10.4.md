# Results vs. 3.10.4

- fork: faster-cpython
- ref: experimental_gc_fix
- machine: linux-x86_64
- commit hash: 9d28e99
- commit date: 2024-09-27
- overall geometric mean: 1.36x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.28x faster
- Memory change: 1.11x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240927-linux-x86_64-faster%2dcpython-experimental_gc_fix-3.14.0a0-9d28e99 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 272 ms: 1.28x faster                                                           |
| docutils       | 3.30 sec                                               | 2.77 sec: 1.19x faster                                                         |
| html5lib       | 88.9 ms                                                | 68.1 ms: 1.31x faster                                                          |
| tornado_http   | 136 ms                                                 | 91.5 ms: 1.49x faster                                                          |
| Geometric mean | (ref)                                                  | 1.31x faster                                                                   |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240927-linux-x86_64-faster%2dcpython-experimental_gc_fix-3.14.0a0-9d28e99 |
|-------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------------:|
| async_tree_memoization  | 870 ms                                                 | 489 ms: 1.78x faster                                                           |
| async_tree_io           | 1.77 sec                                               | 995 ms: 1.78x faster                                                           |
| async_tree_none         | 728 ms                                                 | 424 ms: 1.72x faster                                                           |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 638 ms: 1.59x faster                                                           |
| Geometric mean          | (ref)                                                  | 1.71x faster                                                                   |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240927-linux-x86_64-faster%2dcpython-experimental_gc_fix-3.14.0a0-9d28e99 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 87.7 ms: 1.75x faster                                                          |
| float          | 117 ms                                                 | 97.0 ms: 1.21x faster                                                          |
| pidigits       | 191 ms                                                 | 187 ms: 1.02x faster                                                           |
| Geometric mean | (ref)                                                  | 1.29x faster                                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240927-linux-x86_64-faster%2dcpython-experimental_gc_fix-3.14.0a0-9d28e99 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 128 ms: 1.47x faster                                                           |
| regex_v8       | 27.8 ms                                                | 24.5 ms: 1.13x faster                                                          |
| regex_dna      | 227 ms                                                 | 223 ms: 1.02x faster                                                           |
| Geometric mean | (ref)                                                  | 1.14x faster                                                                   |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240927-linux-x86_64-faster%2dcpython-experimental_gc_fix-3.14.0a0-9d28e99 |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------------------------------:|
| pickle_pure_python   | 484 us                                                 | 305 us: 1.59x faster                                                           |
| unpickle_pure_python | 331 us                                                 | 215 us: 1.54x faster                                                           |
| tomli_loads          | 3.14 sec                                               | 2.09 sec: 1.50x faster                                                         |
| json_dumps           | 14.2 ms                                                | 10.4 ms: 1.36x faster                                                          |
| xml_etree_process    | 79.1 ms                                                | 65.1 ms: 1.22x faster                                                          |
| json_loads           | 31.2 us                                                | 27.1 us: 1.15x faster                                                          |
| xml_etree_generate   | 99.4 ms                                                | 93.0 ms: 1.07x faster                                                          |
| unpickle             | 14.4 us                                                | 14.5 us: 1.01x slower                                                          |
| pickle_list          | 5.08 us                                                | 5.36 us: 1.06x slower                                                          |
| xml_etree_parse      | 168 ms                                                 | 184 ms: 1.10x slower                                                           |
| pickle               | 10.7 us                                                | 11.7 us: 1.10x slower                                                          |
| pickle_dict          | 29.6 us                                                | 34.8 us: 1.18x slower                                                          |
| xml_etree_iterparse  | 115 ms                                                 | 150 ms: 1.30x slower                                                           |
| Geometric mean       | (ref)                                                  | 1.10x faster                                                                   |

Benchmark hidden because not significant (1): unpickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240927-linux-x86_64-faster%2dcpython-experimental_gc_fix-3.14.0a0-9d28e99 |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 10.6 ms: 1.37x faster                                                          |
| python_startup_no_site | 5.93 ms                                                | 7.00 ms: 1.18x slower                                                          |
| Geometric mean         | (ref)                                                  | 1.08x faster                                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240927-linux-x86_64-faster%2dcpython-experimental_gc_fix-3.14.0a0-9d28e99 |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------------------------------:|
| mako            | 16.3 ms                                                | 11.3 ms: 1.44x faster                                                          |
| genshi_text     | 31.8 ms                                                | 22.3 ms: 1.43x faster                                                          |
| django_template | 48.2 ms                                                | 35.2 ms: 1.37x faster                                                          |
| genshi_xml      | 66.0 ms                                                | 54.4 ms: 1.21x faster                                                          |
| Geometric mean  | (ref)                                                  | 1.36x faster                                                                   |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240927-linux-x86_64-faster%2dcpython-experimental_gc_fix-3.14.0a0-9d28e99 |
|--------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 157 us: 3.47x faster                                                           |
| generators               | 80.1 ms                                                | 28.3 ms: 2.83x faster                                                          |
| deltablue                | 7.91 ms                                                | 3.55 ms: 2.23x faster                                                          |
| pylint                   | 551 ms                                                 | 266 ms: 2.07x faster                                                           |
| go                       | 240 ms                                                 | 119 ms: 2.02x faster                                                           |
| chaos                    | 115 ms                                                 | 59.2 ms: 1.95x faster                                                          |
| asyncio_tcp              | 922 ms                                                 | 480 ms: 1.92x faster                                                           |
| raytrace                 | 507 ms                                                 | 264 ms: 1.92x faster                                                           |
| deepcopy_memo            | 58.5 us                                                | 30.6 us: 1.91x faster                                                          |
| deepcopy                 | 479 us                                                 | 261 us: 1.83x faster                                                           |
| richards_super           | 94.7 ms                                                | 52.4 ms: 1.81x faster                                                          |
| logging_silent           | 190 ns                                                 | 105 ns: 1.80x faster                                                           |
| async_tree_memoization   | 870 ms                                                 | 489 ms: 1.78x faster                                                           |
| async_tree_io            | 1.77 sec                                               | 995 ms: 1.78x faster                                                           |
| scimark_sor              | 220 ms                                                 | 125 ms: 1.76x faster                                                           |
| nbody                    | 154 ms                                                 | 87.7 ms: 1.75x faster                                                          |
| crypto_pyaes             | 128 ms                                                 | 73.4 ms: 1.74x faster                                                          |
| scimark_monte_carlo      | 118 ms                                                 | 68.0 ms: 1.74x faster                                                          |
| comprehensions           | 28.8 us                                                | 16.6 us: 1.74x faster                                                          |
| async_tree_none          | 728 ms                                                 | 424 ms: 1.72x faster                                                           |
| richards                 | 79.3 ms                                                | 46.4 ms: 1.71x faster                                                          |
| hexiom                   | 10.4 ms                                                | 6.31 ms: 1.65x faster                                                          |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 638 ms: 1.59x faster                                                           |
| pickle_pure_python       | 484 us                                                 | 305 us: 1.59x faster                                                           |
| sqlglot_parse            | 2.17 ms                                                | 1.41 ms: 1.54x faster                                                          |
| deepcopy_reduce          | 4.17 us                                                | 2.71 us: 1.54x faster                                                          |
| sqlglot_transpile        | 2.57 ms                                                | 1.67 ms: 1.54x faster                                                          |
| unpickle_pure_python     | 331 us                                                 | 215 us: 1.54x faster                                                           |
| spectral_norm            | 170 ms                                                 | 112 ms: 1.52x faster                                                           |
| scimark_lu               | 176 ms                                                 | 116 ms: 1.52x faster                                                           |
| pyflate                  | 716 ms                                                 | 474 ms: 1.51x faster                                                           |
| tomli_loads              | 3.14 sec                                               | 2.09 sec: 1.50x faster                                                         |
| tornado_http             | 136 ms                                                 | 91.5 ms: 1.49x faster                                                          |
| coroutines               | 35.1 ms                                                | 23.6 ms: 1.49x faster                                                          |
| regex_compile            | 188 ms                                                 | 128 ms: 1.47x faster                                                           |
| logging_simple           | 8.30 us                                                | 5.68 us: 1.46x faster                                                          |
| mako                     | 16.3 ms                                                | 11.3 ms: 1.44x faster                                                          |
| asyncio_tcp_ssl          | 2.57 sec                                               | 1.78 sec: 1.44x faster                                                         |
| logging_format           | 9.09 us                                                | 6.34 us: 1.43x faster                                                          |
| pprint_pformat           | 2.10 sec                                               | 1.47 sec: 1.43x faster                                                         |
| genshi_text              | 31.8 ms                                                | 22.3 ms: 1.43x faster                                                          |
| pprint_safe_repr         | 1.02 sec                                               | 717 ms: 1.42x faster                                                           |
| thrift                   | 1.07 ms                                                | 776 us: 1.38x faster                                                           |
| python_startup           | 14.6 ms                                                | 10.6 ms: 1.37x faster                                                          |
| django_template          | 48.2 ms                                                | 35.2 ms: 1.37x faster                                                          |
| json_dumps               | 14.2 ms                                                | 10.4 ms: 1.36x faster                                                          |
| sqlglot_normalize        | 143 ms                                                 | 107 ms: 1.34x faster                                                           |
| sympy_sum                | 196 ms                                                 | 147 ms: 1.33x faster                                                           |
| nqueens                  | 106 ms                                                 | 79.6 ms: 1.33x faster                                                          |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.88 ms: 1.33x faster                                                          |
| sympy_integrate          | 25.8 ms                                                | 19.6 ms: 1.31x faster                                                          |
| fannkuch                 | 532 ms                                                 | 405 ms: 1.31x faster                                                           |
| html5lib                 | 88.9 ms                                                | 68.1 ms: 1.31x faster                                                          |
| dulwich_log              | 84.3 ms                                                | 64.8 ms: 1.30x faster                                                          |
| pycparser                | 1.58 sec                                               | 1.22 sec: 1.29x faster                                                         |
| sympy_str                | 346 ms                                                 | 269 ms: 1.28x faster                                                           |
| 2to3                     | 348 ms                                                 | 272 ms: 1.28x faster                                                           |
| sqlglot_optimize         | 69.2 ms                                                | 54.3 ms: 1.27x faster                                                          |
| pathlib                  | 20.5 ms                                                | 16.1 ms: 1.27x faster                                                          |
| scimark_fft              | 466 ms                                                 | 368 ms: 1.27x faster                                                           |
| bench_thread_pool        | 986 us                                                 | 790 us: 1.25x faster                                                           |
| sympy_expand             | 566 ms                                                 | 458 ms: 1.24x faster                                                           |
| xml_etree_process        | 79.1 ms                                                | 65.1 ms: 1.22x faster                                                          |
| genshi_xml               | 66.0 ms                                                | 54.4 ms: 1.21x faster                                                          |
| unpack_sequence          | 60.0 ns                                                | 49.5 ns: 1.21x faster                                                          |
| float                    | 117 ms                                                 | 97.0 ms: 1.21x faster                                                          |
| docutils                 | 3.30 sec                                               | 2.77 sec: 1.19x faster                                                         |
| json_loads               | 31.2 us                                                | 27.1 us: 1.15x faster                                                          |
| regex_v8                 | 27.8 ms                                                | 24.5 ms: 1.13x faster                                                          |
| json                     | 5.69 ms                                                | 5.13 ms: 1.11x faster                                                          |
| meteor_contest           | 120 ms                                                 | 108 ms: 1.11x faster                                                           |
| sqlite_synth             | 3.02 us                                                | 2.82 us: 1.07x faster                                                          |
| xml_etree_generate       | 99.4 ms                                                | 93.0 ms: 1.07x faster                                                          |
| mdp                      | 2.85 sec                                               | 2.73 sec: 1.04x faster                                                         |
| pidigits                 | 191 ms                                                 | 187 ms: 1.02x faster                                                           |
| regex_dna                | 227 ms                                                 | 223 ms: 1.02x faster                                                           |
| asyncio_websockets       | 559 ms                                                 | 554 ms: 1.01x faster                                                           |
| unpickle                 | 14.4 us                                                | 14.5 us: 1.01x slower                                                          |
| async_generators         | 444 ms                                                 | 459 ms: 1.03x slower                                                           |
| create_gc_cycles         | 1.62 ms                                                | 1.68 ms: 1.04x slower                                                          |
| gc_traversal             | 3.62 ms                                                | 3.77 ms: 1.04x slower                                                          |
| pickle_list              | 5.08 us                                                | 5.36 us: 1.06x slower                                                          |
| coverage                 | 79.4 ms                                                | 86.6 ms: 1.09x slower                                                          |
| xml_etree_parse          | 168 ms                                                 | 184 ms: 1.10x slower                                                           |
| pickle                   | 10.7 us                                                | 11.7 us: 1.10x slower                                                          |
| telco                    | 7.27 ms                                                | 8.42 ms: 1.16x slower                                                          |
| pickle_dict              | 29.6 us                                                | 34.8 us: 1.18x slower                                                          |
| python_startup_no_site   | 5.93 ms                                                | 7.00 ms: 1.18x slower                                                          |
| xml_etree_iterparse      | 115 ms                                                 | 150 ms: 1.30x slower                                                           |
| Geometric mean           | (ref)                                                  | 1.36x faster                                                                   |

Benchmark hidden because not significant (3): bench_mp_pool, unpickle_list, regex_effbot
Ignored benchmarks (9) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (5) of results/bm-20240927-3.14.0a0-9d28e99/bm-20240927-linux-x86_64-faster%2dcpython-experimental_gc_fix-3.14.0a0-9d28e99.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.30x
- 95% likely to have a speedup of 1.29x
- 99% likely to have a speedup of 1.28x

# Memory
- memory change: 1.11x