# Results vs. 3.10.4

- fork: brandtbucher
- ref: no_cold_exits
- machine: linux-x86_64
- commit hash: f837cc6
- commit date: 2024-06-10
- overall geometric mean: 1.34x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.24x faster
- Memory change: 1.18x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240610-linux-x86_64-brandtbucher-no_cold_exits-3.14.0a0-f837cc6 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 277 ms: 1.26x faster                                                 |
| docutils       | 3.30 sec                                               | 2.93 sec: 1.13x faster                                               |
| html5lib       | 88.9 ms                                                | 68.5 ms: 1.30x faster                                                |
| tornado_http   | 136 ms                                                 | 96.9 ms: 1.41x faster                                                |
| Geometric mean | (ref)                                                  | 1.27x faster                                                         |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240610-linux-x86_64-brandtbucher-no_cold_exits-3.14.0a0-f837cc6 |
|-------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| async_tree_none         | 728 ms                                                 | 378 ms: 1.93x faster                                                 |
| async_tree_io           | 1.77 sec                                               | 972 ms: 1.82x faster                                                 |
| async_tree_memoization  | 870 ms                                                 | 482 ms: 1.81x faster                                                 |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 631 ms: 1.61x faster                                                 |
| Geometric mean          | (ref)                                                  | 1.79x faster                                                         |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240610-linux-x86_64-brandtbucher-no_cold_exits-3.14.0a0-f837cc6 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 82.5 ms: 1.86x faster                                                |
| float          | 117 ms                                                 | 72.3 ms: 1.62x faster                                                |
| pidigits       | 191 ms                                                 | 188 ms: 1.02x faster                                                 |
| Geometric mean | (ref)                                                  | 1.45x faster                                                         |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240610-linux-x86_64-brandtbucher-no_cold_exits-3.14.0a0-f837cc6 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 136 ms: 1.38x faster                                                 |
| regex_v8       | 27.8 ms                                                | 24.4 ms: 1.14x faster                                                |
| regex_effbot   | 3.63 ms                                                | 3.55 ms: 1.02x faster                                                |
| regex_dna      | 227 ms                                                 | 226 ms: 1.00x faster                                                 |
| Geometric mean | (ref)                                                  | 1.13x faster                                                         |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240610-linux-x86_64-brandtbucher-no_cold_exits-3.14.0a0-f837cc6 |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| tomli_loads          | 3.14 sec                                               | 1.92 sec: 1.63x faster                                               |
| pickle_pure_python   | 484 us                                                 | 297 us: 1.63x faster                                                 |
| unpickle_pure_python | 331 us                                                 | 222 us: 1.49x faster                                                 |
| json_dumps           | 14.2 ms                                                | 10.4 ms: 1.37x faster                                                |
| xml_etree_process    | 79.1 ms                                                | 59.0 ms: 1.34x faster                                                |
| xml_etree_generate   | 99.4 ms                                                | 82.2 ms: 1.21x faster                                                |
| xml_etree_iterparse  | 115 ms                                                 | 101 ms: 1.15x faster                                                 |
| xml_etree_parse      | 168 ms                                                 | 150 ms: 1.12x faster                                                 |
| json_loads           | 31.2 us                                                | 28.9 us: 1.08x faster                                                |
| unpickle_list        | 5.20 us                                                | 5.44 us: 1.05x slower                                                |
| pickle_list          | 5.08 us                                                | 5.39 us: 1.06x slower                                                |
| unpickle             | 14.4 us                                                | 15.5 us: 1.08x slower                                                |
| pickle               | 10.7 us                                                | 12.0 us: 1.13x slower                                                |
| pickle_dict          | 29.6 us                                                | 36.4 us: 1.23x slower                                                |
| Geometric mean       | (ref)                                                  | 1.15x faster                                                         |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240610-linux-x86_64-brandtbucher-no_cold_exits-3.14.0a0-f837cc6 |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 10.8 ms: 1.35x faster                                                |
| python_startup_no_site | 5.93 ms                                                | 7.20 ms: 1.21x slower                                                |
| Geometric mean         | (ref)                                                  | 1.06x faster                                                         |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240610-linux-x86_64-brandtbucher-no_cold_exits-3.14.0a0-f837cc6 |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| mako            | 16.3 ms                                                | 9.83 ms: 1.66x faster                                                |
| django_template | 48.2 ms                                                | 36.5 ms: 1.32x faster                                                |
| genshi_text     | 31.8 ms                                                | 24.8 ms: 1.28x faster                                                |
| genshi_xml      | 66.0 ms                                                | 58.2 ms: 1.14x faster                                                |
| Geometric mean  | (ref)                                                  | 1.34x faster                                                         |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240610-linux-x86_64-brandtbucher-no_cold_exits-3.14.0a0-f837cc6 |
|--------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 173 us: 3.15x faster                                                 |
| generators               | 80.1 ms                                                | 30.8 ms: 2.60x faster                                                |
| deltablue                | 7.91 ms                                                | 3.73 ms: 2.12x faster                                                |
| richards_super           | 94.7 ms                                                | 47.3 ms: 2.00x faster                                                |
| async_tree_none          | 728 ms                                                 | 378 ms: 1.93x faster                                                 |
| chaos                    | 115 ms                                                 | 60.0 ms: 1.93x faster                                                |
| richards                 | 79.3 ms                                                | 41.8 ms: 1.90x faster                                                |
| crypto_pyaes             | 128 ms                                                 | 67.7 ms: 1.89x faster                                                |
| scimark_monte_carlo      | 118 ms                                                 | 62.8 ms: 1.88x faster                                                |
| nbody                    | 154 ms                                                 | 82.5 ms: 1.86x faster                                                |
| raytrace                 | 507 ms                                                 | 277 ms: 1.83x faster                                                 |
| async_tree_io            | 1.77 sec                                               | 972 ms: 1.82x faster                                                 |
| async_tree_memoization   | 870 ms                                                 | 482 ms: 1.81x faster                                                 |
| logging_silent           | 190 ns                                                 | 106 ns: 1.79x faster                                                 |
| asyncio_tcp              | 922 ms                                                 | 519 ms: 1.78x faster                                                 |
| comprehensions           | 28.8 us                                                | 16.6 us: 1.73x faster                                                |
| spectral_norm            | 170 ms                                                 | 101 ms: 1.68x faster                                                 |
| mako                     | 16.3 ms                                                | 9.83 ms: 1.66x faster                                                |
| sqlglot_parse            | 2.17 ms                                                | 1.31 ms: 1.66x faster                                                |
| tomli_loads              | 3.14 sec                                               | 1.92 sec: 1.63x faster                                               |
| pickle_pure_python       | 484 us                                                 | 297 us: 1.63x faster                                                 |
| go                       | 240 ms                                                 | 147 ms: 1.63x faster                                                 |
| float                    | 117 ms                                                 | 72.3 ms: 1.62x faster                                                |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 631 ms: 1.61x faster                                                 |
| scimark_sor              | 220 ms                                                 | 137 ms: 1.61x faster                                                 |
| pyflate                  | 716 ms                                                 | 456 ms: 1.57x faster                                                 |
| pylint                   | 551 ms                                                 | 352 ms: 1.57x faster                                                 |
| hexiom                   | 10.4 ms                                                | 6.63 ms: 1.57x faster                                                |
| sqlglot_transpile        | 2.57 ms                                                | 1.64 ms: 1.57x faster                                                |
| deepcopy_memo            | 58.5 us                                                | 37.8 us: 1.55x faster                                                |
| coroutines               | 35.1 ms                                                | 22.8 ms: 1.54x faster                                                |
| unpickle_pure_python     | 331 us                                                 | 222 us: 1.49x faster                                                 |
| fannkuch                 | 532 ms                                                 | 358 ms: 1.48x faster                                                 |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.41 ms: 1.47x faster                                                |
| scimark_fft              | 466 ms                                                 | 318 ms: 1.47x faster                                                 |
| logging_simple           | 8.30 us                                                | 5.67 us: 1.46x faster                                                |
| pprint_pformat           | 2.10 sec                                               | 1.45 sec: 1.45x faster                                               |
| logging_format           | 9.09 us                                                | 6.29 us: 1.44x faster                                                |
| pprint_safe_repr         | 1.02 sec                                               | 709 ms: 1.44x faster                                                 |
| tornado_http             | 136 ms                                                 | 96.9 ms: 1.41x faster                                                |
| scimark_lu               | 176 ms                                                 | 125 ms: 1.40x faster                                                 |
| asyncio_tcp_ssl          | 2.57 sec                                               | 1.86 sec: 1.39x faster                                               |
| regex_compile            | 188 ms                                                 | 136 ms: 1.38x faster                                                 |
| pycparser                | 1.58 sec                                               | 1.14 sec: 1.38x faster                                               |
| json_dumps               | 14.2 ms                                                | 10.4 ms: 1.37x faster                                                |
| python_startup           | 14.6 ms                                                | 10.8 ms: 1.35x faster                                                |
| xml_etree_process        | 79.1 ms                                                | 59.0 ms: 1.34x faster                                                |
| django_template          | 48.2 ms                                                | 36.5 ms: 1.32x faster                                                |
| thrift                   | 1.07 ms                                                | 819 us: 1.31x faster                                                 |
| deepcopy                 | 479 us                                                 | 368 us: 1.30x faster                                                 |
| html5lib                 | 88.9 ms                                                | 68.5 ms: 1.30x faster                                                |
| genshi_text              | 31.8 ms                                                | 24.8 ms: 1.28x faster                                                |
| sqlglot_normalize        | 143 ms                                                 | 113 ms: 1.27x faster                                                 |
| deepcopy_reduce          | 4.17 us                                                | 3.30 us: 1.26x faster                                                |
| 2to3                     | 348 ms                                                 | 277 ms: 1.26x faster                                                 |
| pathlib                  | 20.5 ms                                                | 16.3 ms: 1.26x faster                                                |
| dulwich_log              | 84.3 ms                                                | 68.6 ms: 1.23x faster                                                |
| nqueens                  | 106 ms                                                 | 86.2 ms: 1.23x faster                                                |
| sqlglot_optimize         | 69.2 ms                                                | 56.8 ms: 1.22x faster                                                |
| xml_etree_generate       | 99.4 ms                                                | 82.2 ms: 1.21x faster                                                |
| dask                     | 441 ms                                                 | 376 ms: 1.17x faster                                                 |
| sympy_str                | 346 ms                                                 | 299 ms: 1.16x faster                                                 |
| sympy_sum                | 196 ms                                                 | 171 ms: 1.15x faster                                                 |
| xml_etree_iterparse      | 115 ms                                                 | 101 ms: 1.15x faster                                                 |
| sympy_integrate          | 25.8 ms                                                | 22.5 ms: 1.15x faster                                                |
| regex_v8                 | 27.8 ms                                                | 24.4 ms: 1.14x faster                                                |
| genshi_xml               | 66.0 ms                                                | 58.2 ms: 1.14x faster                                                |
| docutils                 | 3.30 sec                                               | 2.93 sec: 1.13x faster                                               |
| bench_thread_pool        | 986 us                                                 | 876 us: 1.13x faster                                                 |
| xml_etree_parse          | 168 ms                                                 | 150 ms: 1.12x faster                                                 |
| sympy_expand             | 566 ms                                                 | 507 ms: 1.12x faster                                                 |
| meteor_contest           | 120 ms                                                 | 108 ms: 1.10x faster                                                 |
| mdp                      | 2.85 sec                                               | 2.58 sec: 1.10x faster                                               |
| json_loads               | 31.2 us                                                | 28.9 us: 1.08x faster                                                |
| json                     | 5.69 ms                                                | 5.32 ms: 1.07x faster                                                |
| sqlite_synth             | 3.02 us                                                | 2.86 us: 1.06x faster                                                |
| regex_effbot             | 3.63 ms                                                | 3.55 ms: 1.02x faster                                                |
| pidigits                 | 191 ms                                                 | 188 ms: 1.02x faster                                                 |
| regex_dna                | 227 ms                                                 | 226 ms: 1.00x faster                                                 |
| asyncio_websockets       | 559 ms                                                 | 566 ms: 1.01x slower                                                 |
| async_generators         | 444 ms                                                 | 464 ms: 1.05x slower                                                 |
| unpickle_list            | 5.20 us                                                | 5.44 us: 1.05x slower                                                |
| pickle_list              | 5.08 us                                                | 5.39 us: 1.06x slower                                                |
| unpickle                 | 14.4 us                                                | 15.5 us: 1.08x slower                                                |
| create_gc_cycles         | 1.62 ms                                                | 1.81 ms: 1.12x slower                                                |
| telco                    | 7.27 ms                                                | 8.12 ms: 1.12x slower                                                |
| gc_traversal             | 3.62 ms                                                | 4.06 ms: 1.12x slower                                                |
| pickle                   | 10.7 us                                                | 12.0 us: 1.13x slower                                                |
| coverage                 | 79.4 ms                                                | 92.8 ms: 1.17x slower                                                |
| python_startup_no_site   | 5.93 ms                                                | 7.20 ms: 1.21x slower                                                |
| pickle_dict              | 29.6 us                                                | 36.4 us: 1.23x slower                                                |
| Geometric mean           | (ref)                                                  | 1.34x faster                                                         |

Benchmark hidden because not significant (1): bench_mp_pool
Ignored benchmarks (9) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, djangocms, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
Ignored benchmarks (4) of results/bm-20240610-3.14.0a0-f837cc6-JIT/bm-20240610-linux-x86_64-brandtbucher-no_cold_exits-3.14.0a0-f837cc6.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.29x
- 95% likely to have a speedup of 1.27x
- 99% likely to have a speedup of 1.24x

# Memory
- memory change: 1.18x