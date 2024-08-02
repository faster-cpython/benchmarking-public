# Results vs. 3.10.4

- fork: python
- ref: e83ce850f433fd8bbf8f
- machine: linux-x86_64
- commit hash: e83ce85
- commit date: 2024-06-05
- overall geometric mean: 1.34x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.23x faster
- Memory change: 1.21x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240605-linux-x86_64-python-e83ce850f433fd8bbf8f-3.14.0a0-e83ce85 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 277 ms: 1.26x faster                                                  |
| docutils       | 3.30 sec                                               | 2.93 sec: 1.13x faster                                                |
| html5lib       | 88.9 ms                                                | 66.6 ms: 1.33x faster                                                 |
| tornado_http   | 136 ms                                                 | 96.7 ms: 1.41x faster                                                 |
| Geometric mean | (ref)                                                  | 1.28x faster                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240605-linux-x86_64-python-e83ce850f433fd8bbf8f-3.14.0a0-e83ce85 |
|-------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_none         | 728 ms                                                 | 378 ms: 1.93x faster                                                  |
| async_tree_memoization  | 870 ms                                                 | 471 ms: 1.85x faster                                                  |
| async_tree_io           | 1.77 sec                                               | 962 ms: 1.84x faster                                                  |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 631 ms: 1.61x faster                                                  |
| Geometric mean          | (ref)                                                  | 1.80x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240605-linux-x86_64-python-e83ce850f433fd8bbf8f-3.14.0a0-e83ce85 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 84.0 ms: 1.83x faster                                                 |
| float          | 117 ms                                                 | 72.3 ms: 1.62x faster                                                 |
| pidigits       | 191 ms                                                 | 188 ms: 1.02x faster                                                  |
| Geometric mean | (ref)                                                  | 1.44x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240605-linux-x86_64-python-e83ce850f433fd8bbf8f-3.14.0a0-e83ce85 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 138 ms: 1.37x faster                                                  |
| regex_v8       | 27.8 ms                                                | 24.5 ms: 1.13x faster                                                 |
| regex_dna      | 227 ms                                                 | 230 ms: 1.01x slower                                                  |
| Geometric mean | (ref)                                                  | 1.11x faster                                                          |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240605-linux-x86_64-python-e83ce850f433fd8bbf8f-3.14.0a0-e83ce85 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| tomli_loads          | 3.14 sec                                               | 1.93 sec: 1.63x faster                                                |
| pickle_pure_python   | 484 us                                                 | 298 us: 1.62x faster                                                  |
| unpickle_pure_python | 331 us                                                 | 222 us: 1.49x faster                                                  |
| json_dumps           | 14.2 ms                                                | 10.4 ms: 1.36x faster                                                 |
| xml_etree_process    | 79.1 ms                                                | 58.2 ms: 1.36x faster                                                 |
| xml_etree_generate   | 99.4 ms                                                | 82.0 ms: 1.21x faster                                                 |
| xml_etree_iterparse  | 115 ms                                                 | 101 ms: 1.14x faster                                                  |
| xml_etree_parse      | 168 ms                                                 | 149 ms: 1.13x faster                                                  |
| json_loads           | 31.2 us                                                | 28.7 us: 1.09x faster                                                 |
| pickle_list          | 5.08 us                                                | 5.23 us: 1.03x slower                                                 |
| unpickle_list        | 5.20 us                                                | 5.39 us: 1.04x slower                                                 |
| unpickle             | 14.4 us                                                | 14.9 us: 1.04x slower                                                 |
| pickle               | 10.7 us                                                | 12.2 us: 1.14x slower                                                 |
| pickle_dict          | 29.6 us                                                | 35.7 us: 1.21x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.16x faster                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240605-linux-x86_64-python-e83ce850f433fd8bbf8f-3.14.0a0-e83ce85 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 11.2 ms: 1.31x faster                                                 |
| python_startup_no_site | 5.93 ms                                                | 7.62 ms: 1.28x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.01x faster                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240605-linux-x86_64-python-e83ce850f433fd8bbf8f-3.14.0a0-e83ce85 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 16.3 ms                                                | 10.0 ms: 1.63x faster                                                 |
| django_template | 48.2 ms                                                | 37.0 ms: 1.30x faster                                                 |
| genshi_text     | 31.8 ms                                                | 25.1 ms: 1.27x faster                                                 |
| genshi_xml      | 66.0 ms                                                | 59.0 ms: 1.12x faster                                                 |
| Geometric mean  | (ref)                                                  | 1.32x faster                                                          |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240605-linux-x86_64-python-e83ce850f433fd8bbf8f-3.14.0a0-e83ce85 |
|--------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 170 us: 3.20x faster                                                  |
| generators               | 80.1 ms                                                | 30.8 ms: 2.60x faster                                                 |
| deltablue                | 7.91 ms                                                | 3.70 ms: 2.14x faster                                                 |
| richards_super           | 94.7 ms                                                | 47.6 ms: 1.99x faster                                                 |
| richards                 | 79.3 ms                                                | 41.1 ms: 1.93x faster                                                 |
| async_tree_none          | 728 ms                                                 | 378 ms: 1.93x faster                                                  |
| chaos                    | 115 ms                                                 | 60.1 ms: 1.92x faster                                                 |
| scimark_monte_carlo      | 118 ms                                                 | 62.6 ms: 1.89x faster                                                 |
| crypto_pyaes             | 128 ms                                                 | 67.7 ms: 1.89x faster                                                 |
| async_tree_memoization   | 870 ms                                                 | 471 ms: 1.85x faster                                                  |
| async_tree_io            | 1.77 sec                                               | 962 ms: 1.84x faster                                                  |
| nbody                    | 154 ms                                                 | 84.0 ms: 1.83x faster                                                 |
| raytrace                 | 507 ms                                                 | 278 ms: 1.82x faster                                                  |
| asyncio_tcp              | 922 ms                                                 | 515 ms: 1.79x faster                                                  |
| logging_silent           | 190 ns                                                 | 107 ns: 1.77x faster                                                  |
| comprehensions           | 28.8 us                                                | 16.7 us: 1.72x faster                                                 |
| scimark_sor              | 220 ms                                                 | 129 ms: 1.70x faster                                                  |
| sqlglot_parse            | 2.17 ms                                                | 1.30 ms: 1.66x faster                                                 |
| spectral_norm            | 170 ms                                                 | 102 ms: 1.66x faster                                                  |
| go                       | 240 ms                                                 | 146 ms: 1.64x faster                                                  |
| mako                     | 16.3 ms                                                | 10.0 ms: 1.63x faster                                                 |
| tomli_loads              | 3.14 sec                                               | 1.93 sec: 1.63x faster                                                |
| pickle_pure_python       | 484 us                                                 | 298 us: 1.62x faster                                                  |
| float                    | 117 ms                                                 | 72.3 ms: 1.62x faster                                                 |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 631 ms: 1.61x faster                                                  |
| pyflate                  | 716 ms                                                 | 452 ms: 1.58x faster                                                  |
| hexiom                   | 10.4 ms                                                | 6.61 ms: 1.57x faster                                                 |
| pylint                   | 551 ms                                                 | 351 ms: 1.57x faster                                                  |
| sqlglot_transpile        | 2.57 ms                                                | 1.64 ms: 1.57x faster                                                 |
| coroutines               | 35.1 ms                                                | 22.9 ms: 1.53x faster                                                 |
| deepcopy_memo            | 58.5 us                                                | 38.5 us: 1.52x faster                                                 |
| fannkuch                 | 532 ms                                                 | 356 ms: 1.49x faster                                                  |
| unpickle_pure_python     | 331 us                                                 | 222 us: 1.49x faster                                                  |
| scimark_fft              | 466 ms                                                 | 319 ms: 1.46x faster                                                  |
| logging_simple           | 8.30 us                                                | 5.69 us: 1.46x faster                                                 |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.49 ms: 1.44x faster                                                 |
| logging_format           | 9.09 us                                                | 6.32 us: 1.44x faster                                                 |
| pprint_pformat           | 2.10 sec                                               | 1.47 sec: 1.43x faster                                                |
| pprint_safe_repr         | 1.02 sec                                               | 720 ms: 1.41x faster                                                  |
| tornado_http             | 136 ms                                                 | 96.7 ms: 1.41x faster                                                 |
| scimark_lu               | 176 ms                                                 | 126 ms: 1.40x faster                                                  |
| asyncio_tcp_ssl          | 2.57 sec                                               | 1.85 sec: 1.39x faster                                                |
| regex_compile            | 188 ms                                                 | 138 ms: 1.37x faster                                                  |
| pycparser                | 1.58 sec                                               | 1.15 sec: 1.37x faster                                                |
| json_dumps               | 14.2 ms                                                | 10.4 ms: 1.36x faster                                                 |
| xml_etree_process        | 79.1 ms                                                | 58.2 ms: 1.36x faster                                                 |
| html5lib                 | 88.9 ms                                                | 66.6 ms: 1.33x faster                                                 |
| thrift                   | 1.07 ms                                                | 810 us: 1.32x faster                                                  |
| python_startup           | 14.6 ms                                                | 11.2 ms: 1.31x faster                                                 |
| django_template          | 48.2 ms                                                | 37.0 ms: 1.30x faster                                                 |
| deepcopy                 | 479 us                                                 | 376 us: 1.27x faster                                                  |
| genshi_text              | 31.8 ms                                                | 25.1 ms: 1.27x faster                                                 |
| deepcopy_reduce          | 4.17 us                                                | 3.30 us: 1.26x faster                                                 |
| 2to3                     | 348 ms                                                 | 277 ms: 1.26x faster                                                  |
| sqlglot_normalize        | 143 ms                                                 | 114 ms: 1.26x faster                                                  |
| pathlib                  | 20.5 ms                                                | 16.4 ms: 1.25x faster                                                 |
| dulwich_log              | 84.3 ms                                                | 68.5 ms: 1.23x faster                                                 |
| xml_etree_generate       | 99.4 ms                                                | 82.0 ms: 1.21x faster                                                 |
| nqueens                  | 106 ms                                                 | 87.3 ms: 1.21x faster                                                 |
| sqlglot_optimize         | 69.2 ms                                                | 57.3 ms: 1.21x faster                                                 |
| dask                     | 441 ms                                                 | 378 ms: 1.17x faster                                                  |
| sympy_integrate          | 25.8 ms                                                | 22.5 ms: 1.15x faster                                                 |
| sympy_str                | 346 ms                                                 | 302 ms: 1.15x faster                                                  |
| sympy_sum                | 196 ms                                                 | 171 ms: 1.15x faster                                                  |
| xml_etree_iterparse      | 115 ms                                                 | 101 ms: 1.14x faster                                                  |
| regex_v8                 | 27.8 ms                                                | 24.5 ms: 1.13x faster                                                 |
| bench_thread_pool        | 986 us                                                 | 873 us: 1.13x faster                                                  |
| docutils                 | 3.30 sec                                               | 2.93 sec: 1.13x faster                                                |
| xml_etree_parse          | 168 ms                                                 | 149 ms: 1.13x faster                                                  |
| genshi_xml               | 66.0 ms                                                | 59.0 ms: 1.12x faster                                                 |
| sympy_expand             | 566 ms                                                 | 510 ms: 1.11x faster                                                  |
| meteor_contest           | 120 ms                                                 | 108 ms: 1.11x faster                                                  |
| json_loads               | 31.2 us                                                | 28.7 us: 1.09x faster                                                 |
| mdp                      | 2.85 sec                                               | 2.63 sec: 1.08x faster                                                |
| json                     | 5.69 ms                                                | 5.37 ms: 1.06x faster                                                 |
| sqlite_synth             | 3.02 us                                                | 2.85 us: 1.06x faster                                                 |
| pidigits                 | 191 ms                                                 | 188 ms: 1.02x faster                                                  |
| regex_dna                | 227 ms                                                 | 230 ms: 1.01x slower                                                  |
| asyncio_websockets       | 559 ms                                                 | 568 ms: 1.02x slower                                                  |
| pickle_list              | 5.08 us                                                | 5.23 us: 1.03x slower                                                 |
| unpickle_list            | 5.20 us                                                | 5.39 us: 1.04x slower                                                 |
| unpickle                 | 14.4 us                                                | 14.9 us: 1.04x slower                                                 |
| async_generators         | 444 ms                                                 | 465 ms: 1.05x slower                                                  |
| gc_traversal             | 3.62 ms                                                | 4.04 ms: 1.11x slower                                                 |
| telco                    | 7.27 ms                                                | 8.10 ms: 1.12x slower                                                 |
| create_gc_cycles         | 1.62 ms                                                | 1.81 ms: 1.12x slower                                                 |
| pickle                   | 10.7 us                                                | 12.2 us: 1.14x slower                                                 |
| coverage                 | 79.4 ms                                                | 92.9 ms: 1.17x slower                                                 |
| pickle_dict              | 29.6 us                                                | 35.7 us: 1.21x slower                                                 |
| python_startup_no_site   | 5.93 ms                                                | 7.62 ms: 1.28x slower                                                 |
| Geometric mean           | (ref)                                                  | 1.34x faster                                                          |

Benchmark hidden because not significant (2): bench_mp_pool, regex_effbot
Ignored benchmarks (9) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, djangocms, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
Ignored benchmarks (4) of results/bm-20240605-3.14.0a0-e83ce85-JIT/bm-20240605-linux-x86_64-python-e83ce850f433fd8bbf8f-3.14.0a0-e83ce85.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.28x
- 95% likely to have a speedup of 1.26x
- 99% likely to have a speedup of 1.23x

# Memory
- memory change: 1.21x