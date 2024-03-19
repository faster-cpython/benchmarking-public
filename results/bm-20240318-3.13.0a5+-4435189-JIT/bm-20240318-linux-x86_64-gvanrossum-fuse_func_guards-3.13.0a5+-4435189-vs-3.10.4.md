# Results vs. 3.10.4

- fork: gvanrossum
- ref: fuse_func_guards
- machine: linux-x86_64
- commit hash: 4435189
- commit date: 2024-03-18
- overall geometric mean: 1.29x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.21x faster
- Memory change: 1.33x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240318-linux-x86_64-gvanrossum-fuse_func_guards-3.13.0a5+-4435189 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 283 ms: 1.23x faster                                                   |
| chameleon      | 9.68 ms                                                | 6.98 ms: 1.39x faster                                                  |
| docutils       | 3.30 sec                                               | 2.77 sec: 1.19x faster                                                 |
| html5lib       | 88.9 ms                                                | 65.9 ms: 1.35x faster                                                  |
| tornado_http   | 136 ms                                                 | 99.0 ms: 1.38x faster                                                  |
| Geometric mean | (ref)                                                  | 1.30x faster                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240318-linux-x86_64-gvanrossum-fuse_func_guards-3.13.0a5+-4435189 |
|-------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_none         | 728 ms                                                 | 445 ms: 1.64x faster                                                   |
| async_tree_memoization  | 870 ms                                                 | 574 ms: 1.52x faster                                                   |
| async_tree_io           | 1.77 sec                                               | 1.21 sec: 1.46x faster                                                 |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 727 ms: 1.40x faster                                                   |
| Geometric mean          | (ref)                                                  | 1.50x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240318-linux-x86_64-gvanrossum-fuse_func_guards-3.13.0a5+-4435189 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 93.2 ms: 1.65x faster                                                  |
| float          | 117 ms                                                 | 80.3 ms: 1.46x faster                                                  |
| pidigits       | 191 ms                                                 | 189 ms: 1.01x faster                                                   |
| Geometric mean | (ref)                                                  | 1.34x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240318-linux-x86_64-gvanrossum-fuse_func_guards-3.13.0a5+-4435189 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 143 ms: 1.32x faster                                                   |
| regex_v8       | 27.8 ms                                                | 25.7 ms: 1.08x faster                                                  |
| regex_dna      | 227 ms                                                 | 224 ms: 1.01x faster                                                   |
| regex_effbot   | 3.63 ms                                                | 3.78 ms: 1.04x slower                                                  |
| Geometric mean | (ref)                                                  | 1.09x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240318-linux-x86_64-gvanrossum-fuse_func_guards-3.13.0a5+-4435189 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| pickle_pure_python   | 484 us                                                 | 306 us: 1.58x faster                                                   |
| tomli_loads          | 3.14 sec                                               | 2.09 sec: 1.51x faster                                                 |
| unpickle_pure_python | 331 us                                                 | 239 us: 1.39x faster                                                   |
| json_dumps           | 14.2 ms                                                | 10.6 ms: 1.34x faster                                                  |
| xml_etree_process    | 79.1 ms                                                | 60.4 ms: 1.31x faster                                                  |
| xml_etree_generate   | 99.4 ms                                                | 87.9 ms: 1.13x faster                                                  |
| json_loads           | 31.2 us                                                | 27.9 us: 1.12x faster                                                  |
| xml_etree_iterparse  | 115 ms                                                 | 109 ms: 1.06x faster                                                   |
| xml_etree_parse      | 168 ms                                                 | 160 ms: 1.05x faster                                                   |
| unpickle_list        | 5.20 us                                                | 5.07 us: 1.02x faster                                                  |
| pickle_list          | 5.08 us                                                | 5.01 us: 1.01x faster                                                  |
| unpickle             | 14.4 us                                                | 15.5 us: 1.08x slower                                                  |
| pickle               | 10.7 us                                                | 11.6 us: 1.08x slower                                                  |
| pickle_dict          | 29.6 us                                                | 33.7 us: 1.14x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.14x faster                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240318-linux-x86_64-gvanrossum-fuse_func_guards-3.13.0a5+-4435189 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 12.6 ms: 1.16x faster                                                  |
| python_startup_no_site | 5.93 ms                                                | 11.2 ms: 1.88x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.28x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240318-linux-x86_64-gvanrossum-fuse_func_guards-3.13.0a5+-4435189 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| mako            | 16.3 ms                                                | 11.0 ms: 1.49x faster                                                  |
| django_template | 48.2 ms                                                | 34.5 ms: 1.39x faster                                                  |
| genshi_text     | 31.8 ms                                                | 25.0 ms: 1.27x faster                                                  |
| genshi_xml      | 66.0 ms                                                | 56.5 ms: 1.17x faster                                                  |
| Geometric mean  | (ref)                                                  | 1.33x faster                                                           |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240318-linux-x86_64-gvanrossum-fuse_func_guards-3.13.0a5+-4435189 |
|--------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 112 us: 4.87x faster                                                   |
| generators               | 80.1 ms                                                | 29.6 ms: 2.70x faster                                                  |
| deltablue                | 7.91 ms                                                | 3.45 ms: 2.29x faster                                                  |
| logging_silent           | 190 ns                                                 | 100 ns: 1.90x faster                                                   |
| asyncio_tcp              | 922 ms                                                 | 504 ms: 1.83x faster                                                   |
| richards_super           | 94.7 ms                                                | 52.6 ms: 1.80x faster                                                  |
| chaos                    | 115 ms                                                 | 64.2 ms: 1.80x faster                                                  |
| raytrace                 | 507 ms                                                 | 293 ms: 1.73x faster                                                   |
| richards                 | 79.3 ms                                                | 46.5 ms: 1.70x faster                                                  |
| pylint                   | 551 ms                                                 | 324 ms: 1.70x faster                                                   |
| crypto_pyaes             | 128 ms                                                 | 75.9 ms: 1.68x faster                                                  |
| scimark_sor              | 220 ms                                                 | 131 ms: 1.68x faster                                                   |
| scimark_monte_carlo      | 118 ms                                                 | 70.7 ms: 1.67x faster                                                  |
| nbody                    | 154 ms                                                 | 93.2 ms: 1.65x faster                                                  |
| comprehensions           | 28.8 us                                                | 17.5 us: 1.65x faster                                                  |
| sqlglot_parse            | 2.17 ms                                                | 1.32 ms: 1.64x faster                                                  |
| async_tree_none          | 728 ms                                                 | 445 ms: 1.64x faster                                                   |
| pickle_pure_python       | 484 us                                                 | 306 us: 1.58x faster                                                   |
| sqlglot_transpile        | 2.57 ms                                                | 1.66 ms: 1.55x faster                                                  |
| coroutines               | 35.1 ms                                                | 22.9 ms: 1.53x faster                                                  |
| go                       | 240 ms                                                 | 158 ms: 1.52x faster                                                   |
| async_tree_memoization   | 870 ms                                                 | 574 ms: 1.52x faster                                                   |
| tomli_loads              | 3.14 sec                                               | 2.09 sec: 1.51x faster                                                 |
| deepcopy_memo            | 58.5 us                                                | 39.0 us: 1.50x faster                                                  |
| spectral_norm            | 170 ms                                                 | 114 ms: 1.49x faster                                                   |
| pyflate                  | 716 ms                                                 | 481 ms: 1.49x faster                                                   |
| mako                     | 16.3 ms                                                | 11.0 ms: 1.49x faster                                                  |
| hexiom                   | 10.4 ms                                                | 7.04 ms: 1.48x faster                                                  |
| float                    | 117 ms                                                 | 80.3 ms: 1.46x faster                                                  |
| async_tree_io            | 1.77 sec                                               | 1.21 sec: 1.46x faster                                                 |
| logging_simple           | 8.30 us                                                | 5.89 us: 1.41x faster                                                  |
| logging_format           | 9.09 us                                                | 6.50 us: 1.40x faster                                                  |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 727 ms: 1.40x faster                                                   |
| django_template          | 48.2 ms                                                | 34.5 ms: 1.39x faster                                                  |
| asyncio_tcp_ssl          | 2.57 sec                                               | 1.85 sec: 1.39x faster                                                 |
| chameleon                | 9.68 ms                                                | 6.98 ms: 1.39x faster                                                  |
| unpickle_pure_python     | 331 us                                                 | 239 us: 1.39x faster                                                   |
| tornado_http             | 136 ms                                                 | 99.0 ms: 1.38x faster                                                  |
| deepcopy                 | 479 us                                                 | 348 us: 1.38x faster                                                   |
| deepcopy_reduce          | 4.17 us                                                | 3.08 us: 1.36x faster                                                  |
| pprint_pformat           | 2.10 sec                                               | 1.55 sec: 1.35x faster                                                 |
| html5lib                 | 88.9 ms                                                | 65.9 ms: 1.35x faster                                                  |
| scimark_fft              | 466 ms                                                 | 346 ms: 1.35x faster                                                   |
| pprint_safe_repr         | 1.02 sec                                               | 758 ms: 1.34x faster                                                   |
| json_dumps               | 14.2 ms                                                | 10.6 ms: 1.34x faster                                                  |
| fannkuch                 | 532 ms                                                 | 397 ms: 1.34x faster                                                   |
| thrift                   | 1.07 ms                                                | 802 us: 1.34x faster                                                   |
| scimark_lu               | 176 ms                                                 | 132 ms: 1.33x faster                                                   |
| sqlglot_normalize        | 143 ms                                                 | 108 ms: 1.32x faster                                                   |
| regex_compile            | 188 ms                                                 | 143 ms: 1.32x faster                                                   |
| xml_etree_process        | 79.1 ms                                                | 60.4 ms: 1.31x faster                                                  |
| pycparser                | 1.58 sec                                               | 1.20 sec: 1.31x faster                                                 |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.96 ms: 1.30x faster                                                  |
| genshi_text              | 31.8 ms                                                | 25.0 ms: 1.27x faster                                                  |
| 2to3                     | 348 ms                                                 | 283 ms: 1.23x faster                                                   |
| djangocms                | 38.4 us                                                | 31.4 us: 1.22x faster                                                  |
| sympy_integrate          | 25.8 ms                                                | 21.2 ms: 1.21x faster                                                  |
| sqlglot_optimize         | 69.2 ms                                                | 57.1 ms: 1.21x faster                                                  |
| sympy_sum                | 196 ms                                                 | 162 ms: 1.21x faster                                                   |
| dulwich_log              | 84.3 ms                                                | 69.7 ms: 1.21x faster                                                  |
| sympy_str                | 346 ms                                                 | 287 ms: 1.20x faster                                                   |
| aiohttp                  | 1.44 ms                                                | 1.20 ms: 1.20x faster                                                  |
| docutils                 | 3.30 sec                                               | 2.77 sec: 1.19x faster                                                 |
| dask                     | 441 ms                                                 | 373 ms: 1.18x faster                                                   |
| gunicorn                 | 1.53 ms                                                | 1.30 ms: 1.18x faster                                                  |
| nqueens                  | 106 ms                                                 | 90.2 ms: 1.17x faster                                                  |
| genshi_xml               | 66.0 ms                                                | 56.5 ms: 1.17x faster                                                  |
| sympy_expand             | 566 ms                                                 | 487 ms: 1.16x faster                                                   |
| python_startup           | 14.6 ms                                                | 12.6 ms: 1.16x faster                                                  |
| bench_thread_pool        | 986 us                                                 | 855 us: 1.15x faster                                                   |
| xml_etree_generate       | 99.4 ms                                                | 87.9 ms: 1.13x faster                                                  |
| json_loads               | 31.2 us                                                | 27.9 us: 1.12x faster                                                  |
| json                     | 5.69 ms                                                | 5.12 ms: 1.11x faster                                                  |
| regex_v8                 | 27.8 ms                                                | 25.7 ms: 1.08x faster                                                  |
| meteor_contest           | 120 ms                                                 | 111 ms: 1.08x faster                                                   |
| mdp                      | 2.85 sec                                               | 2.65 sec: 1.08x faster                                                 |
| create_gc_cycles         | 1.62 ms                                                | 1.51 ms: 1.07x faster                                                  |
| pathlib                  | 20.5 ms                                                | 19.1 ms: 1.07x faster                                                  |
| sqlite_synth             | 3.02 us                                                | 2.83 us: 1.07x faster                                                  |
| xml_etree_iterparse      | 115 ms                                                 | 109 ms: 1.06x faster                                                   |
| xml_etree_parse          | 168 ms                                                 | 160 ms: 1.05x faster                                                   |
| unpickle_list            | 5.20 us                                                | 5.07 us: 1.02x faster                                                  |
| pickle_list              | 5.08 us                                                | 5.01 us: 1.01x faster                                                  |
| regex_dna                | 227 ms                                                 | 224 ms: 1.01x faster                                                   |
| pidigits                 | 191 ms                                                 | 189 ms: 1.01x faster                                                   |
| asyncio_websockets       | 559 ms                                                 | 564 ms: 1.01x slower                                                   |
| regex_effbot             | 3.63 ms                                                | 3.78 ms: 1.04x slower                                                  |
| async_generators         | 444 ms                                                 | 468 ms: 1.05x slower                                                   |
| unpickle                 | 14.4 us                                                | 15.5 us: 1.08x slower                                                  |
| gc_traversal             | 3.62 ms                                                | 3.92 ms: 1.08x slower                                                  |
| pickle                   | 10.7 us                                                | 11.6 us: 1.08x slower                                                  |
| bench_mp_pool            | 24.0 ms                                                | 26.4 ms: 1.10x slower                                                  |
| pickle_dict              | 29.6 us                                                | 33.7 us: 1.14x slower                                                  |
| telco                    | 7.27 ms                                                | 8.44 ms: 1.16x slower                                                  |
| coverage                 | 79.4 ms                                                | 98.6 ms: 1.24x slower                                                  |
| unpack_sequence          | 60.0 ns                                                | 86.8 ns: 1.45x slower                                                  |
| python_startup_no_site   | 5.93 ms                                                | 11.2 ms: 1.88x slower                                                  |
| Geometric mean           | (ref)                                                  | 1.29x faster                                                           |

Benchmark hidden because not significant (1): mypy2
Ignored benchmarks (3) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: flaskblogging, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (4) of results/bm-20240318-3.13.0a5+-4435189-JIT/bm-20240318-linux-x86_64-gvanrossum-fuse_func_guards-3.13.0a5+-4435189.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.26x
- 95% likely to have a speedup of 1.23x
- 99% likely to have a speedup of 1.21x


# Memory

- memory change: 1.33x