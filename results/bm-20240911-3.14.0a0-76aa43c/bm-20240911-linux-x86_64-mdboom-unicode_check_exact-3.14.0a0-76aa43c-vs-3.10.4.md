# Results vs. 3.10.4

- fork: mdboom
- ref: unicode_check_exact
- machine: linux-x86_64
- commit hash: 76aa43c
- commit date: 2024-09-11
- overall geometric mean: 1.40x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.31x faster
- Memory change: 1.12x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240911-linux-x86_64-mdboom-unicode_check_exact-3.14.0a0-76aa43c |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 255 ms: 1.37x faster                                                 |
| docutils       | 3.30 sec                                               | 2.66 sec: 1.24x faster                                               |
| html5lib       | 88.9 ms                                                | 63.0 ms: 1.41x faster                                                |
| tornado_http   | 136 ms                                                 | 90.4 ms: 1.51x faster                                                |
| Geometric mean | (ref)                                                  | 1.38x faster                                                         |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240911-linux-x86_64-mdboom-unicode_check_exact-3.14.0a0-76aa43c |
|-------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| async_tree_none         | 728 ms                                                 | 313 ms: 2.32x faster                                                 |
| async_tree_memoization  | 870 ms                                                 | 391 ms: 2.22x faster                                                 |
| async_tree_io           | 1.77 sec                                               | 861 ms: 2.06x faster                                                 |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 559 ms: 1.82x faster                                                 |
| Geometric mean          | (ref)                                                  | 2.10x faster                                                         |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240911-linux-x86_64-mdboom-unicode_check_exact-3.14.0a0-76aa43c |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 89.4 ms: 1.72x faster                                                |
| float          | 117 ms                                                 | 77.7 ms: 1.51x faster                                                |
| pidigits       | 191 ms                                                 | 187 ms: 1.02x faster                                                 |
| Geometric mean | (ref)                                                  | 1.38x faster                                                         |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240911-linux-x86_64-mdboom-unicode_check_exact-3.14.0a0-76aa43c |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 130 ms: 1.45x faster                                                 |
| regex_v8       | 27.8 ms                                                | 24.8 ms: 1.12x faster                                                |
| regex_dna      | 227 ms                                                 | 217 ms: 1.05x faster                                                 |
| regex_effbot   | 3.63 ms                                                | 3.53 ms: 1.03x faster                                                |
| Geometric mean | (ref)                                                  | 1.15x faster                                                         |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240911-linux-x86_64-mdboom-unicode_check_exact-3.14.0a0-76aa43c |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| pickle_pure_python   | 484 us                                                 | 301 us: 1.61x faster                                                 |
| unpickle_pure_python | 331 us                                                 | 213 us: 1.55x faster                                                 |
| tomli_loads          | 3.14 sec                                               | 2.08 sec: 1.51x faster                                               |
| json_dumps           | 14.2 ms                                                | 10.4 ms: 1.36x faster                                                |
| xml_etree_process    | 79.1 ms                                                | 59.3 ms: 1.33x faster                                                |
| json_loads           | 31.2 us                                                | 26.7 us: 1.17x faster                                                |
| xml_etree_generate   | 99.4 ms                                                | 85.6 ms: 1.16x faster                                                |
| xml_etree_iterparse  | 115 ms                                                 | 104 ms: 1.11x faster                                                 |
| xml_etree_parse      | 168 ms                                                 | 154 ms: 1.09x faster                                                 |
| unpickle_list        | 5.20 us                                                | 5.44 us: 1.05x slower                                                |
| pickle               | 10.7 us                                                | 11.4 us: 1.07x slower                                                |
| unpickle             | 14.4 us                                                | 15.6 us: 1.08x slower                                                |
| pickle_dict          | 29.6 us                                                | 34.9 us: 1.18x slower                                                |
| Geometric mean       | (ref)                                                  | 1.16x faster                                                         |

Benchmark hidden because not significant (1): pickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240911-linux-x86_64-mdboom-unicode_check_exact-3.14.0a0-76aa43c |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 10.5 ms: 1.39x faster                                                |
| python_startup_no_site | 5.93 ms                                                | 6.97 ms: 1.18x slower                                                |
| Geometric mean         | (ref)                                                  | 1.09x faster                                                         |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240911-linux-x86_64-mdboom-unicode_check_exact-3.14.0a0-76aa43c |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| mako            | 16.3 ms                                                | 11.2 ms: 1.46x faster                                                |
| django_template | 48.2 ms                                                | 34.8 ms: 1.38x faster                                                |
| genshi_text     | 31.8 ms                                                | 23.1 ms: 1.38x faster                                                |
| genshi_xml      | 66.0 ms                                                | 52.2 ms: 1.27x faster                                                |
| Geometric mean  | (ref)                                                  | 1.37x faster                                                         |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240911-linux-x86_64-mdboom-unicode_check_exact-3.14.0a0-76aa43c |
|--------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 161 us: 3.39x faster                                                 |
| generators               | 80.1 ms                                                | 27.9 ms: 2.87x faster                                                |
| deltablue                | 7.91 ms                                                | 3.19 ms: 2.48x faster                                                |
| async_tree_none          | 728 ms                                                 | 313 ms: 2.32x faster                                                 |
| async_tree_memoization   | 870 ms                                                 | 391 ms: 2.22x faster                                                 |
| async_tree_io            | 1.77 sec                                               | 861 ms: 2.06x faster                                                 |
| go                       | 240 ms                                                 | 117 ms: 2.04x faster                                                 |
| chaos                    | 115 ms                                                 | 58.9 ms: 1.96x faster                                                |
| raytrace                 | 507 ms                                                 | 259 ms: 1.96x faster                                                 |
| asyncio_tcp              | 922 ms                                                 | 475 ms: 1.94x faster                                                 |
| deepcopy_memo            | 58.5 us                                                | 30.8 us: 1.90x faster                                                |
| logging_silent           | 190 ns                                                 | 100 ns: 1.89x faster                                                 |
| deepcopy                 | 479 us                                                 | 261 us: 1.84x faster                                                 |
| richards_super           | 94.7 ms                                                | 51.9 ms: 1.82x faster                                                |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 559 ms: 1.82x faster                                                 |
| crypto_pyaes             | 128 ms                                                 | 71.8 ms: 1.78x faster                                                |
| comprehensions           | 28.8 us                                                | 16.4 us: 1.76x faster                                                |
| scimark_monte_carlo      | 118 ms                                                 | 67.8 ms: 1.74x faster                                                |
| scimark_sor              | 220 ms                                                 | 127 ms: 1.74x faster                                                 |
| richards                 | 79.3 ms                                                | 46.0 ms: 1.72x faster                                                |
| pylint                   | 551 ms                                                 | 320 ms: 1.72x faster                                                 |
| nbody                    | 154 ms                                                 | 89.4 ms: 1.72x faster                                                |
| sqlglot_parse            | 2.17 ms                                                | 1.29 ms: 1.69x faster                                                |
| hexiom                   | 10.4 ms                                                | 6.22 ms: 1.67x faster                                                |
| sqlglot_transpile        | 2.57 ms                                                | 1.58 ms: 1.62x faster                                                |
| pickle_pure_python       | 484 us                                                 | 301 us: 1.61x faster                                                 |
| deepcopy_reduce          | 4.17 us                                                | 2.67 us: 1.56x faster                                                |
| unpickle_pure_python     | 331 us                                                 | 213 us: 1.55x faster                                                 |
| scimark_lu               | 176 ms                                                 | 114 ms: 1.54x faster                                                 |
| spectral_norm            | 170 ms                                                 | 112 ms: 1.51x faster                                                 |
| pyflate                  | 716 ms                                                 | 474 ms: 1.51x faster                                                 |
| tomli_loads              | 3.14 sec                                               | 2.08 sec: 1.51x faster                                               |
| tornado_http             | 136 ms                                                 | 90.4 ms: 1.51x faster                                                |
| float                    | 117 ms                                                 | 77.7 ms: 1.51x faster                                                |
| coroutines               | 35.1 ms                                                | 23.6 ms: 1.49x faster                                                |
| mako                     | 16.3 ms                                                | 11.2 ms: 1.46x faster                                                |
| regex_compile            | 188 ms                                                 | 130 ms: 1.45x faster                                                 |
| logging_simple           | 8.30 us                                                | 5.74 us: 1.45x faster                                                |
| asyncio_tcp_ssl          | 2.57 sec                                               | 1.79 sec: 1.44x faster                                               |
| pprint_pformat           | 2.10 sec                                               | 1.47 sec: 1.43x faster                                               |
| logging_format           | 9.09 us                                                | 6.38 us: 1.42x faster                                                |
| pprint_safe_repr         | 1.02 sec                                               | 718 ms: 1.42x faster                                                 |
| html5lib                 | 88.9 ms                                                | 63.0 ms: 1.41x faster                                                |
| python_startup           | 14.6 ms                                                | 10.5 ms: 1.39x faster                                                |
| thrift                   | 1.07 ms                                                | 770 us: 1.39x faster                                                 |
| pycparser                | 1.58 sec                                               | 1.14 sec: 1.39x faster                                               |
| django_template          | 48.2 ms                                                | 34.8 ms: 1.38x faster                                                |
| genshi_text              | 31.8 ms                                                | 23.1 ms: 1.38x faster                                                |
| 2to3                     | 348 ms                                                 | 255 ms: 1.37x faster                                                 |
| json_dumps               | 14.2 ms                                                | 10.4 ms: 1.36x faster                                                |
| sympy_sum                | 196 ms                                                 | 147 ms: 1.34x faster                                                 |
| nqueens                  | 106 ms                                                 | 79.3 ms: 1.33x faster                                                |
| xml_etree_process        | 79.1 ms                                                | 59.3 ms: 1.33x faster                                                |
| fannkuch                 | 532 ms                                                 | 403 ms: 1.32x faster                                                 |
| sympy_integrate          | 25.8 ms                                                | 19.6 ms: 1.32x faster                                                |
| sqlglot_normalize        | 143 ms                                                 | 109 ms: 1.32x faster                                                 |
| dulwich_log              | 84.3 ms                                                | 64.5 ms: 1.31x faster                                                |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.98 ms: 1.30x faster                                                |
| sqlglot_optimize         | 69.2 ms                                                | 53.7 ms: 1.29x faster                                                |
| pathlib                  | 20.5 ms                                                | 15.9 ms: 1.29x faster                                                |
| sympy_str                | 346 ms                                                 | 270 ms: 1.28x faster                                                 |
| genshi_xml               | 66.0 ms                                                | 52.2 ms: 1.27x faster                                                |
| scimark_fft              | 466 ms                                                 | 371 ms: 1.26x faster                                                 |
| bench_thread_pool        | 986 us                                                 | 789 us: 1.25x faster                                                 |
| docutils                 | 3.30 sec                                               | 2.66 sec: 1.24x faster                                               |
| sympy_expand             | 566 ms                                                 | 460 ms: 1.23x faster                                                 |
| unpack_sequence          | 60.0 ns                                                | 50.5 ns: 1.19x faster                                                |
| json_loads               | 31.2 us                                                | 26.7 us: 1.17x faster                                                |
| xml_etree_generate       | 99.4 ms                                                | 85.6 ms: 1.16x faster                                                |
| json                     | 5.69 ms                                                | 4.92 ms: 1.16x faster                                                |
| regex_v8                 | 27.8 ms                                                | 24.8 ms: 1.12x faster                                                |
| xml_etree_iterparse      | 115 ms                                                 | 104 ms: 1.11x faster                                                 |
| meteor_contest           | 120 ms                                                 | 108 ms: 1.11x faster                                                 |
| mdp                      | 2.85 sec                                               | 2.58 sec: 1.10x faster                                               |
| xml_etree_parse          | 168 ms                                                 | 154 ms: 1.09x faster                                                 |
| sqlite_synth             | 3.02 us                                                | 2.85 us: 1.06x faster                                                |
| regex_dna                | 227 ms                                                 | 217 ms: 1.05x faster                                                 |
| async_generators         | 444 ms                                                 | 427 ms: 1.04x faster                                                 |
| regex_effbot             | 3.63 ms                                                | 3.53 ms: 1.03x faster                                                |
| pidigits                 | 191 ms                                                 | 187 ms: 1.02x faster                                                 |
| asyncio_websockets       | 559 ms                                                 | 554 ms: 1.01x faster                                                 |
| gc_traversal             | 3.62 ms                                                | 3.66 ms: 1.01x slower                                                |
| unpickle_list            | 5.20 us                                                | 5.44 us: 1.05x slower                                                |
| create_gc_cycles         | 1.62 ms                                                | 1.71 ms: 1.06x slower                                                |
| pickle                   | 10.7 us                                                | 11.4 us: 1.07x slower                                                |
| unpickle                 | 14.4 us                                                | 15.6 us: 1.08x slower                                                |
| coverage                 | 79.4 ms                                                | 86.5 ms: 1.09x slower                                                |
| telco                    | 7.27 ms                                                | 8.42 ms: 1.16x slower                                                |
| python_startup_no_site   | 5.93 ms                                                | 6.97 ms: 1.18x slower                                                |
| pickle_dict              | 29.6 us                                                | 34.9 us: 1.18x slower                                                |
| Geometric mean           | (ref)                                                  | 1.40x faster                                                         |

Benchmark hidden because not significant (2): pickle_list, bench_mp_pool
Ignored benchmarks (9) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (5) of results/bm-20240911-3.14.0a0-76aa43c/bm-20240911-linux-x86_64-mdboom-unicode_check_exact-3.14.0a0-76aa43c.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.34x
- 95% likely to have a speedup of 1.33x
- 99% likely to have a speedup of 1.31x

# Memory
- memory change: 1.12x