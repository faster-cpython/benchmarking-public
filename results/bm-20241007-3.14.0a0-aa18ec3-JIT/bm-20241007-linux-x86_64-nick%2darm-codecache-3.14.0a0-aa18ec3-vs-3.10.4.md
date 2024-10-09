# Results vs. 3.10.4

- fork: nick-arm
- ref: codecache
- machine: linux-x86_64
- commit hash: aa18ec3
- commit date: 2024-10-07
- overall geometric mean: 1.36x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.25x faster
- Memory change: 1.20x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241007-linux-x86_64-nick%2darm-codecache-3.14.0a0-aa18ec3 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 278 ms: 1.25x faster                                           |
| docutils       | 3.30 sec                                               | 2.94 sec: 1.12x faster                                         |
| html5lib       | 88.9 ms                                                | 65.0 ms: 1.37x faster                                          |
| tornado_http   | 136 ms                                                 | 95.6 ms: 1.43x faster                                          |
| Geometric mean | (ref)                                                  | 1.29x faster                                                   |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241007-linux-x86_64-nick%2darm-codecache-3.14.0a0-aa18ec3 |
|-------------------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| async_tree_none         | 728 ms                                                 | 319 ms: 2.29x faster                                           |
| async_tree_memoization  | 870 ms                                                 | 406 ms: 2.14x faster                                           |
| async_tree_io           | 1.77 sec                                               | 886 ms: 2.00x faster                                           |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 575 ms: 1.77x faster                                           |
| Geometric mean          | (ref)                                                  | 2.04x faster                                                   |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241007-linux-x86_64-nick%2darm-codecache-3.14.0a0-aa18ec3 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 80.1 ms: 1.92x faster                                          |
| float          | 117 ms                                                 | 71.9 ms: 1.63x faster                                          |
| pidigits       | 191 ms                                                 | 185 ms: 1.03x faster                                           |
| Geometric mean | (ref)                                                  | 1.48x faster                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241007-linux-x86_64-nick%2darm-codecache-3.14.0a0-aa18ec3 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 143 ms: 1.32x faster                                           |
| regex_v8       | 27.8 ms                                                | 26.4 ms: 1.05x faster                                          |
| regex_dna      | 227 ms                                                 | 227 ms: 1.00x slower                                           |
| Geometric mean | (ref)                                                  | 1.08x faster                                                   |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241007-linux-x86_64-nick%2darm-codecache-3.14.0a0-aa18ec3 |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| tomli_loads          | 3.14 sec                                               | 1.93 sec: 1.62x faster                                         |
| pickle_pure_python   | 484 us                                                 | 302 us: 1.60x faster                                           |
| unpickle_pure_python | 331 us                                                 | 216 us: 1.53x faster                                           |
| xml_etree_process    | 79.1 ms                                                | 54.7 ms: 1.45x faster                                          |
| json_dumps           | 14.2 ms                                                | 10.2 ms: 1.39x faster                                          |
| xml_etree_generate   | 99.4 ms                                                | 77.6 ms: 1.28x faster                                          |
| xml_etree_iterparse  | 115 ms                                                 | 98.2 ms: 1.18x faster                                          |
| xml_etree_parse      | 168 ms                                                 | 145 ms: 1.16x faster                                           |
| json_loads           | 31.2 us                                                | 27.0 us: 1.15x faster                                          |
| pickle_list          | 5.08 us                                                | 5.13 us: 1.01x slower                                          |
| unpickle_list        | 5.20 us                                                | 5.29 us: 1.02x slower                                          |
| pickle               | 10.7 us                                                | 11.8 us: 1.11x slower                                          |
| pickle_dict          | 29.6 us                                                | 35.5 us: 1.20x slower                                          |
| Geometric mean       | (ref)                                                  | 1.19x faster                                                   |

Benchmark hidden because not significant (1): unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241007-linux-x86_64-nick%2darm-codecache-3.14.0a0-aa18ec3 |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 10.6 ms: 1.38x faster                                          |
| python_startup_no_site | 5.93 ms                                                | 7.10 ms: 1.20x slower                                          |
| Geometric mean         | (ref)                                                  | 1.07x faster                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241007-linux-x86_64-nick%2darm-codecache-3.14.0a0-aa18ec3 |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| mako            | 16.3 ms                                                | 9.94 ms: 1.64x faster                                          |
| django_template | 48.2 ms                                                | 35.8 ms: 1.35x faster                                          |
| genshi_text     | 31.8 ms                                                | 25.4 ms: 1.25x faster                                          |
| genshi_xml      | 66.0 ms                                                | 58.2 ms: 1.14x faster                                          |
| Geometric mean  | (ref)                                                  | 1.33x faster                                                   |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241007-linux-x86_64-nick%2darm-codecache-3.14.0a0-aa18ec3 |
|--------------------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 163 us: 3.34x faster                                           |
| deltablue                | 7.91 ms                                                | 3.21 ms: 2.46x faster                                          |
| async_tree_none          | 728 ms                                                 | 319 ms: 2.29x faster                                           |
| generators               | 80.1 ms                                                | 35.1 ms: 2.28x faster                                          |
| deepcopy_memo            | 58.5 us                                                | 27.1 us: 2.15x faster                                          |
| async_tree_memoization   | 870 ms                                                 | 406 ms: 2.14x faster                                           |
| richards_super           | 94.7 ms                                                | 45.8 ms: 2.07x faster                                          |
| async_tree_io            | 1.77 sec                                               | 886 ms: 2.00x faster                                           |
| richards                 | 79.3 ms                                                | 41.0 ms: 1.93x faster                                          |
| nbody                    | 154 ms                                                 | 80.1 ms: 1.92x faster                                          |
| chaos                    | 115 ms                                                 | 60.7 ms: 1.90x faster                                          |
| logging_silent           | 190 ns                                                 | 100.0 ns: 1.90x faster                                         |
| crypto_pyaes             | 128 ms                                                 | 67.4 ms: 1.90x faster                                          |
| asyncio_tcp              | 922 ms                                                 | 493 ms: 1.87x faster                                           |
| scimark_sor              | 220 ms                                                 | 118 ms: 1.86x faster                                           |
| scimark_monte_carlo      | 118 ms                                                 | 64.0 ms: 1.85x faster                                          |
| raytrace                 | 507 ms                                                 | 276 ms: 1.84x faster                                           |
| deepcopy                 | 479 us                                                 | 263 us: 1.82x faster                                           |
| go                       | 240 ms                                                 | 134 ms: 1.79x faster                                           |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 575 ms: 1.77x faster                                           |
| comprehensions           | 28.8 us                                                | 17.0 us: 1.69x faster                                          |
| spectral_norm            | 170 ms                                                 | 102 ms: 1.67x faster                                           |
| mako                     | 16.3 ms                                                | 9.94 ms: 1.64x faster                                          |
| float                    | 117 ms                                                 | 71.9 ms: 1.63x faster                                          |
| tomli_loads              | 3.14 sec                                               | 1.93 sec: 1.62x faster                                         |
| sqlglot_parse            | 2.17 ms                                                | 1.34 ms: 1.62x faster                                          |
| scimark_lu               | 176 ms                                                 | 110 ms: 1.61x faster                                           |
| pickle_pure_python       | 484 us                                                 | 302 us: 1.60x faster                                           |
| deepcopy_reduce          | 4.17 us                                                | 2.66 us: 1.57x faster                                          |
| pyflate                  | 716 ms                                                 | 457 ms: 1.57x faster                                           |
| unpickle_pure_python     | 331 us                                                 | 216 us: 1.53x faster                                           |
| scimark_fft              | 466 ms                                                 | 305 ms: 1.53x faster                                           |
| sqlglot_transpile        | 2.57 ms                                                | 1.69 ms: 1.52x faster                                          |
| coroutines               | 35.1 ms                                                | 23.0 ms: 1.52x faster                                          |
| hexiom                   | 10.4 ms                                                | 6.99 ms: 1.49x faster                                          |
| pylint                   | 551 ms                                                 | 373 ms: 1.48x faster                                           |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.37 ms: 1.48x faster                                          |
| logging_format           | 9.09 us                                                | 6.19 us: 1.47x faster                                          |
| logging_simple           | 8.30 us                                                | 5.67 us: 1.47x faster                                          |
| pprint_safe_repr         | 1.02 sec                                               | 698 ms: 1.46x faster                                           |
| pprint_pformat           | 2.10 sec                                               | 1.45 sec: 1.45x faster                                         |
| xml_etree_process        | 79.1 ms                                                | 54.7 ms: 1.45x faster                                          |
| tornado_http             | 136 ms                                                 | 95.6 ms: 1.43x faster                                          |
| asyncio_tcp_ssl          | 2.57 sec                                               | 1.80 sec: 1.42x faster                                         |
| fannkuch                 | 532 ms                                                 | 374 ms: 1.42x faster                                           |
| json_dumps               | 14.2 ms                                                | 10.2 ms: 1.39x faster                                          |
| python_startup           | 14.6 ms                                                | 10.6 ms: 1.38x faster                                          |
| html5lib                 | 88.9 ms                                                | 65.0 ms: 1.37x faster                                          |
| thrift                   | 1.07 ms                                                | 790 us: 1.36x faster                                           |
| django_template          | 48.2 ms                                                | 35.8 ms: 1.35x faster                                          |
| regex_compile            | 188 ms                                                 | 143 ms: 1.32x faster                                           |
| pycparser                | 1.58 sec                                               | 1.21 sec: 1.30x faster                                         |
| pathlib                  | 20.5 ms                                                | 15.9 ms: 1.29x faster                                          |
| xml_etree_generate       | 99.4 ms                                                | 77.6 ms: 1.28x faster                                          |
| genshi_text              | 31.8 ms                                                | 25.4 ms: 1.25x faster                                          |
| 2to3                     | 348 ms                                                 | 278 ms: 1.25x faster                                           |
| sqlglot_normalize        | 143 ms                                                 | 115 ms: 1.24x faster                                           |
| nqueens                  | 106 ms                                                 | 85.8 ms: 1.23x faster                                          |
| dulwich_log              | 84.3 ms                                                | 68.5 ms: 1.23x faster                                          |
| xml_etree_iterparse      | 115 ms                                                 | 98.2 ms: 1.18x faster                                          |
| xml_etree_parse          | 168 ms                                                 | 145 ms: 1.16x faster                                           |
| sqlglot_optimize         | 69.2 ms                                                | 59.9 ms: 1.16x faster                                          |
| json_loads               | 31.2 us                                                | 27.0 us: 1.15x faster                                          |
| sympy_str                | 346 ms                                                 | 300 ms: 1.15x faster                                           |
| json                     | 5.69 ms                                                | 4.96 ms: 1.15x faster                                          |
| genshi_xml               | 66.0 ms                                                | 58.2 ms: 1.14x faster                                          |
| sympy_expand             | 566 ms                                                 | 499 ms: 1.13x faster                                           |
| docutils                 | 3.30 sec                                               | 2.94 sec: 1.12x faster                                         |
| meteor_contest           | 120 ms                                                 | 108 ms: 1.11x faster                                           |
| sympy_sum                | 196 ms                                                 | 177 ms: 1.11x faster                                           |
| sqlite_synth             | 3.02 us                                                | 2.73 us: 1.11x faster                                          |
| sympy_integrate          | 25.8 ms                                                | 23.4 ms: 1.10x faster                                          |
| bench_thread_pool        | 986 us                                                 | 897 us: 1.10x faster                                           |
| regex_v8                 | 27.8 ms                                                | 26.4 ms: 1.05x faster                                          |
| mdp                      | 2.85 sec                                               | 2.71 sec: 1.05x faster                                         |
| pidigits                 | 191 ms                                                 | 185 ms: 1.03x faster                                           |
| regex_dna                | 227 ms                                                 | 227 ms: 1.00x slower                                           |
| pickle_list              | 5.08 us                                                | 5.13 us: 1.01x slower                                          |
| unpickle_list            | 5.20 us                                                | 5.29 us: 1.02x slower                                          |
| async_generators         | 444 ms                                                 | 457 ms: 1.03x slower                                           |
| gc_traversal             | 3.62 ms                                                | 3.75 ms: 1.03x slower                                          |
| telco                    | 7.27 ms                                                | 7.62 ms: 1.05x slower                                          |
| create_gc_cycles         | 1.62 ms                                                | 1.73 ms: 1.07x slower                                          |
| coverage                 | 79.4 ms                                                | 85.8 ms: 1.08x slower                                          |
| pickle                   | 10.7 us                                                | 11.8 us: 1.11x slower                                          |
| python_startup_no_site   | 5.93 ms                                                | 7.10 ms: 1.20x slower                                          |
| pickle_dict              | 29.6 us                                                | 35.5 us: 1.20x slower                                          |
| unpack_sequence          | 60.0 ns                                                | 110 ns: 1.83x slower                                           |
| bench_mp_pool            | 24.0 ms                                                | 61.3 ms: 2.55x slower                                          |
| Geometric mean           | (ref)                                                  | 1.36x faster                                                   |

Benchmark hidden because not significant (3): asyncio_websockets, regex_effbot, unpickle
Ignored benchmarks (9) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (5) of results/bm-20241007-3.14.0a0-aa18ec3-JIT/bm-20241007-linux-x86_64-nick%2darm-codecache-3.14.0a0-aa18ec3.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.29x
- 95% likely to have a speedup of 1.27x
- 99% likely to have a speedup of 1.25x

# Memory
- memory change: 1.20x