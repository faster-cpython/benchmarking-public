# Results vs. 3.10.4

- fork: python
- ref: e418fc3a6e7bade68ab5
- machine: linux-x86_64
- commit hash: e418fc3
- commit date: 2024-05-25
- overall geometric mean: 1.01x faster
- HPT reliability: 96.70%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.13x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240525-linux-x86_64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 375 ms: 1.08x slower                                                  |
| chameleon      | 9.68 ms                                                | 8.91 ms: 1.09x faster                                                 |
| docutils       | 3.30 sec                                               | 3.51 sec: 1.07x slower                                                |
| html5lib       | 88.9 ms                                                | 82.2 ms: 1.08x faster                                                 |
| tornado_http   | 136 ms                                                 | 107 ms: 1.27x faster                                                  |
| Geometric mean | (ref)                                                  | 1.05x faster                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240525-linux-x86_64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|-------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_io           | 1.77 sec                                               | 1.03 sec: 1.72x faster                                                |
| async_tree_none         | 728 ms                                                 | 428 ms: 1.70x faster                                                  |
| async_tree_memoization  | 870 ms                                                 | 531 ms: 1.64x faster                                                  |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 665 ms: 1.53x faster                                                  |
| Geometric mean          | (ref)                                                  | 1.64x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240525-linux-x86_64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| pidigits       | 191 ms                                                 | 194 ms: 1.01x slower                                                  |
| float          | 117 ms                                                 | 130 ms: 1.11x slower                                                  |
| nbody          | 154 ms                                                 | 193 ms: 1.26x slower                                                  |
| Geometric mean | (ref)                                                  | 1.12x slower                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240525-linux-x86_64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_v8       | 27.8 ms                                                | 26.9 ms: 1.03x faster                                                 |
| regex_dna      | 227 ms                                                 | 235 ms: 1.04x slower                                                  |
| regex_effbot   | 3.63 ms                                                | 3.87 ms: 1.07x slower                                                 |
| regex_compile  | 188 ms                                                 | 236 ms: 1.25x slower                                                  |
| Geometric mean | (ref)                                                  | 1.08x slower                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240525-linux-x86_64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| json_dumps           | 14.2 ms                                                | 11.7 ms: 1.21x faster                                                 |
| xml_etree_parse      | 168 ms                                                 | 155 ms: 1.09x faster                                                  |
| json_loads           | 31.2 us                                                | 29.0 us: 1.08x faster                                                 |
| xml_etree_process    | 79.1 ms                                                | 78.3 ms: 1.01x faster                                                 |
| pickle_list          | 5.08 us                                                | 5.23 us: 1.03x slower                                                 |
| unpickle             | 14.4 us                                                | 15.2 us: 1.06x slower                                                 |
| xml_etree_iterparse  | 115 ms                                                 | 125 ms: 1.09x slower                                                  |
| tomli_loads          | 3.14 sec                                               | 3.49 sec: 1.11x slower                                                |
| xml_etree_generate   | 99.4 ms                                                | 114 ms: 1.14x slower                                                  |
| pickle               | 10.7 us                                                | 12.2 us: 1.15x slower                                                 |
| pickle_pure_python   | 484 us                                                 | 560 us: 1.16x slower                                                  |
| unpickle_pure_python | 331 us                                                 | 396 us: 1.20x slower                                                  |
| pickle_dict          | 29.6 us                                                | 35.5 us: 1.20x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.05x slower                                                          |

Benchmark hidden because not significant (1): unpickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240525-linux-x86_64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 10.7 ms: 1.37x faster                                                 |
| python_startup_no_site | 5.93 ms                                                | 7.18 ms: 1.21x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.06x faster                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240525-linux-x86_64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| django_template | 48.2 ms                                                | 49.6 ms: 1.03x slower                                                 |
| mako            | 16.3 ms                                                | 19.9 ms: 1.22x slower                                                 |
| genshi_xml      | 66.0 ms                                                | 85.5 ms: 1.29x slower                                                 |
| genshi_text     | 31.8 ms                                                | 41.3 ms: 1.30x slower                                                 |
| Geometric mean  | (ref)                                                  | 1.20x slower                                                          |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240525-linux-x86_64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|--------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 216 us: 2.52x faster                                                  |
| generators               | 80.1 ms                                                | 31.9 ms: 2.51x faster                                                 |
| asyncio_tcp              | 922 ms                                                 | 525 ms: 1.75x faster                                                  |
| async_tree_io            | 1.77 sec                                               | 1.03 sec: 1.72x faster                                                |
| async_tree_none          | 728 ms                                                 | 428 ms: 1.70x faster                                                  |
| async_tree_memoization   | 870 ms                                                 | 531 ms: 1.64x faster                                                  |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 665 ms: 1.53x faster                                                  |
| deltablue                | 7.91 ms                                                | 5.33 ms: 1.49x faster                                                 |
| coroutines               | 35.1 ms                                                | 24.2 ms: 1.45x faster                                                 |
| pylint                   | 551 ms                                                 | 388 ms: 1.42x faster                                                  |
| asyncio_tcp_ssl          | 2.57 sec                                               | 1.87 sec: 1.37x faster                                                |
| python_startup           | 14.6 ms                                                | 10.7 ms: 1.37x faster                                                 |
| raytrace                 | 507 ms                                                 | 384 ms: 1.32x faster                                                  |
| thrift                   | 1.07 ms                                                | 831 us: 1.29x faster                                                  |
| tornado_http             | 136 ms                                                 | 107 ms: 1.27x faster                                                  |
| logging_simple           | 8.30 us                                                | 6.65 us: 1.25x faster                                                 |
| scimark_sor              | 220 ms                                                 | 179 ms: 1.23x faster                                                  |
| logging_format           | 9.09 us                                                | 7.42 us: 1.23x faster                                                 |
| json_dumps               | 14.2 ms                                                | 11.7 ms: 1.21x faster                                                 |
| pathlib                  | 20.5 ms                                                | 18.0 ms: 1.14x faster                                                 |
| dask                     | 441 ms                                                 | 394 ms: 1.12x faster                                                  |
| dulwich_log              | 84.3 ms                                                | 77.3 ms: 1.09x faster                                                 |
| xml_etree_parse          | 168 ms                                                 | 155 ms: 1.09x faster                                                  |
| chameleon                | 9.68 ms                                                | 8.91 ms: 1.09x faster                                                 |
| html5lib                 | 88.9 ms                                                | 82.2 ms: 1.08x faster                                                 |
| go                       | 240 ms                                                 | 222 ms: 1.08x faster                                                  |
| json_loads               | 31.2 us                                                | 29.0 us: 1.08x faster                                                 |
| richards_super           | 94.7 ms                                                | 88.1 ms: 1.08x faster                                                 |
| chaos                    | 115 ms                                                 | 109 ms: 1.06x faster                                                  |
| regex_v8                 | 27.8 ms                                                | 26.9 ms: 1.03x faster                                                 |
| sqlglot_parse            | 2.17 ms                                                | 2.14 ms: 1.02x faster                                                 |
| json                     | 5.69 ms                                                | 5.62 ms: 1.01x faster                                                 |
| xml_etree_process        | 79.1 ms                                                | 78.3 ms: 1.01x faster                                                 |
| bench_thread_pool        | 986 us                                                 | 996 us: 1.01x slower                                                  |
| pidigits                 | 191 ms                                                 | 194 ms: 1.01x slower                                                  |
| asyncio_websockets       | 559 ms                                                 | 567 ms: 1.01x slower                                                  |
| sympy_sum                | 196 ms                                                 | 199 ms: 1.02x slower                                                  |
| pycparser                | 1.58 sec                                               | 1.61 sec: 1.02x slower                                                |
| richards                 | 79.3 ms                                                | 81.0 ms: 1.02x slower                                                 |
| django_template          | 48.2 ms                                                | 49.6 ms: 1.03x slower                                                 |
| pickle_list              | 5.08 us                                                | 5.23 us: 1.03x slower                                                 |
| sqlite_synth             | 3.02 us                                                | 3.13 us: 1.04x slower                                                 |
| regex_dna                | 227 ms                                                 | 235 ms: 1.04x slower                                                  |
| deepcopy_reduce          | 4.17 us                                                | 4.38 us: 1.05x slower                                                 |
| sqlglot_normalize        | 143 ms                                                 | 150 ms: 1.05x slower                                                  |
| unpickle                 | 14.4 us                                                | 15.2 us: 1.06x slower                                                 |
| docutils                 | 3.30 sec                                               | 3.51 sec: 1.07x slower                                                |
| regex_effbot             | 3.63 ms                                                | 3.87 ms: 1.07x slower                                                 |
| mdp                      | 2.85 sec                                               | 3.05 sec: 1.07x slower                                                |
| gc_traversal             | 3.62 ms                                                | 3.89 ms: 1.07x slower                                                 |
| 2to3                     | 348 ms                                                 | 375 ms: 1.08x slower                                                  |
| xml_etree_iterparse      | 115 ms                                                 | 125 ms: 1.09x slower                                                  |
| sympy_expand             | 566 ms                                                 | 615 ms: 1.09x slower                                                  |
| sqlglot_optimize         | 69.2 ms                                                | 75.6 ms: 1.09x slower                                                 |
| sympy_str                | 346 ms                                                 | 378 ms: 1.09x slower                                                  |
| sympy_integrate          | 25.8 ms                                                | 28.2 ms: 1.09x slower                                                 |
| float                    | 117 ms                                                 | 130 ms: 1.11x slower                                                  |
| tomli_loads              | 3.14 sec                                               | 3.49 sec: 1.11x slower                                                |
| scimark_lu               | 176 ms                                                 | 196 ms: 1.11x slower                                                  |
| flaskblogging            | 8.58 ms                                                | 9.56 ms: 1.12x slower                                                 |
| async_generators         | 444 ms                                                 | 496 ms: 1.12x slower                                                  |
| create_gc_cycles         | 1.62 ms                                                | 1.84 ms: 1.13x slower                                                 |
| xml_etree_generate       | 99.4 ms                                                | 114 ms: 1.14x slower                                                  |
| scimark_monte_carlo      | 118 ms                                                 | 135 ms: 1.15x slower                                                  |
| pickle                   | 10.7 us                                                | 12.2 us: 1.15x slower                                                 |
| pyflate                  | 716 ms                                                 | 826 ms: 1.15x slower                                                  |
| pickle_pure_python       | 484 us                                                 | 560 us: 1.16x slower                                                  |
| deepcopy                 | 479 us                                                 | 554 us: 1.16x slower                                                  |
| logging_silent           | 190 ns                                                 | 222 ns: 1.17x slower                                                  |
| coverage                 | 79.4 ms                                                | 94.1 ms: 1.18x slower                                                 |
| unpickle_pure_python     | 331 us                                                 | 396 us: 1.20x slower                                                  |
| pickle_dict              | 29.6 us                                                | 35.5 us: 1.20x slower                                                 |
| python_startup_no_site   | 5.93 ms                                                | 7.18 ms: 1.21x slower                                                 |
| meteor_contest           | 120 ms                                                 | 145 ms: 1.21x slower                                                  |
| mako                     | 16.3 ms                                                | 19.9 ms: 1.22x slower                                                 |
| pprint_safe_repr         | 1.02 sec                                               | 1.27 sec: 1.24x slower                                                |
| pprint_pformat           | 2.10 sec                                               | 2.63 sec: 1.25x slower                                                |
| regex_compile            | 188 ms                                                 | 236 ms: 1.25x slower                                                  |
| nbody                    | 154 ms                                                 | 193 ms: 1.26x slower                                                  |
| spectral_norm            | 170 ms                                                 | 216 ms: 1.27x slower                                                  |
| scimark_fft              | 466 ms                                                 | 598 ms: 1.28x slower                                                  |
| genshi_xml               | 66.0 ms                                                | 85.5 ms: 1.29x slower                                                 |
| genshi_text              | 31.8 ms                                                | 41.3 ms: 1.30x slower                                                 |
| comprehensions           | 28.8 us                                                | 37.6 us: 1.31x slower                                                 |
| fannkuch                 | 532 ms                                                 | 701 ms: 1.32x slower                                                  |
| deepcopy_memo            | 58.5 us                                                | 77.8 us: 1.33x slower                                                 |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 8.72 ms: 1.35x slower                                                 |
| nqueens                  | 106 ms                                                 | 145 ms: 1.37x slower                                                  |
| hexiom                   | 10.4 ms                                                | 15.0 ms: 1.44x slower                                                 |
| telco                    | 7.27 ms                                                | 10.6 ms: 1.46x slower                                                 |
| Geometric mean           | (ref)                                                  | 1.01x faster                                                          |

Benchmark hidden because not significant (4): unpickle_list, bench_mp_pool, sqlglot_transpile, crypto_pyaes
Ignored benchmarks (7) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, djangocms, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
Ignored benchmarks (4) of results/bm-20240525-3.14.0a0-e418fc3-PYTHON_UOPS/bm-20240525-linux-x86_64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg

# HPT report

- Reliability score: 96.70% likely to be slow
- 90% likely to have a slowdown of 1.01x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.13x