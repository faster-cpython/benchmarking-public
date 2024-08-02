# Results vs. 3.10.4

- fork: brandtbucher
- ref: no_cold_exits
- machine: linux-x86_64
- commit hash: a1bdb94
- commit date: 2024-06-18
- overall geometric mean: 1.35x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.24x faster
- Memory change: 1.18x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240618-linux-x86_64-brandtbucher-no_cold_exits-3.14.0a0-a1bdb94 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 279 ms: 1.25x faster                                                 |
| html5lib       | 88.9 ms                                                | 68.9 ms: 1.29x faster                                                |
| tornado_http   | 136 ms                                                 | 96.3 ms: 1.42x faster                                                |
| Geometric mean | (ref)                                                  | 1.32x faster                                                         |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240618-linux-x86_64-brandtbucher-no_cold_exits-3.14.0a0-a1bdb94 |
|-------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| async_tree_none         | 728 ms                                                 | 372 ms: 1.96x faster                                                 |
| async_tree_io           | 1.77 sec                                               | 943 ms: 1.88x faster                                                 |
| async_tree_memoization  | 870 ms                                                 | 486 ms: 1.79x faster                                                 |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 629 ms: 1.62x faster                                                 |
| Geometric mean          | (ref)                                                  | 1.80x faster                                                         |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240618-linux-x86_64-brandtbucher-no_cold_exits-3.14.0a0-a1bdb94 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 82.2 ms: 1.87x faster                                                |
| float          | 117 ms                                                 | 71.8 ms: 1.63x faster                                                |
| pidigits       | 191 ms                                                 | 189 ms: 1.01x faster                                                 |
| Geometric mean | (ref)                                                  | 1.45x faster                                                         |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240618-linux-x86_64-brandtbucher-no_cold_exits-3.14.0a0-a1bdb94 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 138 ms: 1.37x faster                                                 |
| regex_v8       | 27.8 ms                                                | 26.4 ms: 1.05x faster                                                |
| regex_dna      | 227 ms                                                 | 236 ms: 1.04x slower                                                 |
| regex_effbot   | 3.63 ms                                                | 3.99 ms: 1.10x slower                                                |
| Geometric mean | (ref)                                                  | 1.06x faster                                                         |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240618-linux-x86_64-brandtbucher-no_cold_exits-3.14.0a0-a1bdb94 |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| pickle_pure_python   | 484 us                                                 | 297 us: 1.63x faster                                                 |
| tomli_loads          | 3.14 sec                                               | 1.97 sec: 1.60x faster                                               |
| unpickle_pure_python | 331 us                                                 | 222 us: 1.49x faster                                                 |
| json_dumps           | 14.2 ms                                                | 10.5 ms: 1.35x faster                                                |
| xml_etree_process    | 79.1 ms                                                | 59.3 ms: 1.33x faster                                                |
| xml_etree_generate   | 99.4 ms                                                | 82.7 ms: 1.20x faster                                                |
| xml_etree_iterparse  | 115 ms                                                 | 101 ms: 1.15x faster                                                 |
| xml_etree_parse      | 168 ms                                                 | 148 ms: 1.14x faster                                                 |
| json_loads           | 31.2 us                                                | 28.8 us: 1.08x faster                                                |
| unpickle             | 14.4 us                                                | 14.8 us: 1.03x slower                                                |
| pickle_list          | 5.08 us                                                | 5.29 us: 1.04x slower                                                |
| pickle               | 10.7 us                                                | 11.9 us: 1.12x slower                                                |
| pickle_dict          | 29.6 us                                                | 36.1 us: 1.22x slower                                                |
| Geometric mean       | (ref)                                                  | 1.16x faster                                                         |

Benchmark hidden because not significant (1): unpickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240618-linux-x86_64-brandtbucher-no_cold_exits-3.14.0a0-a1bdb94 |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 10.8 ms: 1.35x faster                                                |
| python_startup_no_site | 5.93 ms                                                | 7.25 ms: 1.22x slower                                                |
| Geometric mean         | (ref)                                                  | 1.05x faster                                                         |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240618-linux-x86_64-brandtbucher-no_cold_exits-3.14.0a0-a1bdb94 |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| mako            | 16.3 ms                                                | 9.92 ms: 1.64x faster                                                |
| django_template | 48.2 ms                                                | 37.0 ms: 1.30x faster                                                |
| genshi_text     | 31.8 ms                                                | 25.1 ms: 1.27x faster                                                |
| genshi_xml      | 66.0 ms                                                | 58.2 ms: 1.14x faster                                                |
| Geometric mean  | (ref)                                                  | 1.33x faster                                                         |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240618-linux-x86_64-brandtbucher-no_cold_exits-3.14.0a0-a1bdb94 |
|--------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 168 us: 3.23x faster                                                 |
| generators               | 80.1 ms                                                | 30.0 ms: 2.67x faster                                                |
| deltablue                | 7.91 ms                                                | 3.63 ms: 2.18x faster                                                |
| deepcopy_memo            | 58.5 us                                                | 29.0 us: 2.02x faster                                                |
| richards_super           | 94.7 ms                                                | 48.3 ms: 1.96x faster                                                |
| async_tree_none          | 728 ms                                                 | 372 ms: 1.96x faster                                                 |
| chaos                    | 115 ms                                                 | 60.0 ms: 1.92x faster                                                |
| scimark_monte_carlo      | 118 ms                                                 | 62.6 ms: 1.89x faster                                                |
| async_tree_io            | 1.77 sec                                               | 943 ms: 1.88x faster                                                 |
| nbody                    | 154 ms                                                 | 82.2 ms: 1.87x faster                                                |
| crypto_pyaes             | 128 ms                                                 | 68.5 ms: 1.87x faster                                                |
| richards                 | 79.3 ms                                                | 42.6 ms: 1.86x faster                                                |
| raytrace                 | 507 ms                                                 | 275 ms: 1.84x faster                                                 |
| async_tree_memoization   | 870 ms                                                 | 486 ms: 1.79x faster                                                 |
| asyncio_tcp              | 922 ms                                                 | 517 ms: 1.78x faster                                                 |
| logging_silent           | 190 ns                                                 | 108 ns: 1.76x faster                                                 |
| deepcopy                 | 479 us                                                 | 276 us: 1.74x faster                                                 |
| comprehensions           | 28.8 us                                                | 16.8 us: 1.72x faster                                                |
| sqlglot_parse            | 2.17 ms                                                | 1.32 ms: 1.65x faster                                                |
| mako                     | 16.3 ms                                                | 9.92 ms: 1.64x faster                                                |
| float                    | 117 ms                                                 | 71.8 ms: 1.63x faster                                                |
| pickle_pure_python       | 484 us                                                 | 297 us: 1.63x faster                                                 |
| go                       | 240 ms                                                 | 148 ms: 1.62x faster                                                 |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 629 ms: 1.62x faster                                                 |
| spectral_norm            | 170 ms                                                 | 106 ms: 1.60x faster                                                 |
| tomli_loads              | 3.14 sec                                               | 1.97 sec: 1.60x faster                                               |
| scimark_sor              | 220 ms                                                 | 140 ms: 1.57x faster                                                 |
| pylint                   | 551 ms                                                 | 353 ms: 1.56x faster                                                 |
| pyflate                  | 716 ms                                                 | 459 ms: 1.56x faster                                                 |
| sqlglot_transpile        | 2.57 ms                                                | 1.65 ms: 1.56x faster                                                |
| hexiom                   | 10.4 ms                                                | 6.72 ms: 1.55x faster                                                |
| coroutines               | 35.1 ms                                                | 22.9 ms: 1.53x faster                                                |
| deepcopy_reduce          | 4.17 us                                                | 2.73 us: 1.53x faster                                                |
| logging_simple           | 8.30 us                                                | 5.54 us: 1.50x faster                                                |
| unpickle_pure_python     | 331 us                                                 | 222 us: 1.49x faster                                                 |
| fannkuch                 | 532 ms                                                 | 359 ms: 1.48x faster                                                 |
| logging_format           | 9.09 us                                                | 6.23 us: 1.46x faster                                                |
| pprint_pformat           | 2.10 sec                                               | 1.47 sec: 1.43x faster                                               |
| scimark_fft              | 466 ms                                                 | 326 ms: 1.43x faster                                                 |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.57 ms: 1.42x faster                                                |
| tornado_http             | 136 ms                                                 | 96.3 ms: 1.42x faster                                                |
| pprint_safe_repr         | 1.02 sec                                               | 720 ms: 1.41x faster                                                 |
| scimark_lu               | 176 ms                                                 | 125 ms: 1.41x faster                                                 |
| asyncio_tcp_ssl          | 2.57 sec                                               | 1.85 sec: 1.39x faster                                               |
| regex_compile            | 188 ms                                                 | 138 ms: 1.37x faster                                                 |
| python_startup           | 14.6 ms                                                | 10.8 ms: 1.35x faster                                                |
| json_dumps               | 14.2 ms                                                | 10.5 ms: 1.35x faster                                                |
| pycparser                | 1.58 sec                                               | 1.17 sec: 1.34x faster                                               |
| xml_etree_process        | 79.1 ms                                                | 59.3 ms: 1.33x faster                                                |
| django_template          | 48.2 ms                                                | 37.0 ms: 1.30x faster                                                |
| thrift                   | 1.07 ms                                                | 830 us: 1.29x faster                                                 |
| html5lib                 | 88.9 ms                                                | 68.9 ms: 1.29x faster                                                |
| genshi_text              | 31.8 ms                                                | 25.1 ms: 1.27x faster                                                |
| nqueens                  | 106 ms                                                 | 84.3 ms: 1.26x faster                                                |
| 2to3                     | 348 ms                                                 | 279 ms: 1.25x faster                                                 |
| pathlib                  | 20.5 ms                                                | 16.4 ms: 1.25x faster                                                |
| sqlglot_normalize        | 143 ms                                                 | 115 ms: 1.24x faster                                                 |
| dulwich_log              | 84.3 ms                                                | 68.8 ms: 1.23x faster                                                |
| sqlglot_optimize         | 69.2 ms                                                | 57.1 ms: 1.21x faster                                                |
| xml_etree_generate       | 99.4 ms                                                | 82.7 ms: 1.20x faster                                                |
| dask                     | 441 ms                                                 | 376 ms: 1.17x faster                                                 |
| bench_thread_pool        | 986 us                                                 | 850 us: 1.16x faster                                                 |
| sympy_sum                | 196 ms                                                 | 171 ms: 1.15x faster                                                 |
| xml_etree_iterparse      | 115 ms                                                 | 101 ms: 1.15x faster                                                 |
| sympy_str                | 346 ms                                                 | 303 ms: 1.14x faster                                                 |
| sympy_integrate          | 25.8 ms                                                | 22.7 ms: 1.14x faster                                                |
| xml_etree_parse          | 168 ms                                                 | 148 ms: 1.14x faster                                                 |
| genshi_xml               | 66.0 ms                                                | 58.2 ms: 1.14x faster                                                |
| sympy_expand             | 566 ms                                                 | 512 ms: 1.10x faster                                                 |
| mdp                      | 2.85 sec                                               | 2.58 sec: 1.10x faster                                               |
| meteor_contest           | 120 ms                                                 | 109 ms: 1.09x faster                                                 |
| json_loads               | 31.2 us                                                | 28.8 us: 1.08x faster                                                |
| json                     | 5.69 ms                                                | 5.33 ms: 1.07x faster                                                |
| sqlite_synth             | 3.02 us                                                | 2.85 us: 1.06x faster                                                |
| regex_v8                 | 27.8 ms                                                | 26.4 ms: 1.05x faster                                                |
| pidigits                 | 191 ms                                                 | 189 ms: 1.01x faster                                                 |
| asyncio_websockets       | 559 ms                                                 | 566 ms: 1.01x slower                                                 |
| unpickle                 | 14.4 us                                                | 14.8 us: 1.03x slower                                                |
| pickle_list              | 5.08 us                                                | 5.29 us: 1.04x slower                                                |
| regex_dna                | 227 ms                                                 | 236 ms: 1.04x slower                                                 |
| async_generators         | 444 ms                                                 | 465 ms: 1.05x slower                                                 |
| gc_traversal             | 3.62 ms                                                | 3.92 ms: 1.08x slower                                                |
| regex_effbot             | 3.63 ms                                                | 3.99 ms: 1.10x slower                                                |
| create_gc_cycles         | 1.62 ms                                                | 1.79 ms: 1.10x slower                                                |
| telco                    | 7.27 ms                                                | 8.04 ms: 1.11x slower                                                |
| pickle                   | 10.7 us                                                | 11.9 us: 1.12x slower                                                |
| coverage                 | 79.4 ms                                                | 95.2 ms: 1.20x slower                                                |
| pickle_dict              | 29.6 us                                                | 36.1 us: 1.22x slower                                                |
| python_startup_no_site   | 5.93 ms                                                | 7.25 ms: 1.22x slower                                                |
| Geometric mean           | (ref)                                                  | 1.35x faster                                                         |

Benchmark hidden because not significant (2): bench_mp_pool, unpickle_list
Ignored benchmarks (10) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, djangocms, docutils, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
Ignored benchmarks (5) of results/bm-20240618-3.14.0a0-a1bdb94-JIT/bm-20240618-linux-x86_64-brandtbucher-no_cold_exits-3.14.0a0-a1bdb94.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.29x
- 95% likely to have a speedup of 1.27x
- 99% likely to have a speedup of 1.24x

# Memory
- memory change: 1.18x