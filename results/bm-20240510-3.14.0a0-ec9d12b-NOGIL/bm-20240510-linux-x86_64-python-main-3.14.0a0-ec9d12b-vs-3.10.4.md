# Results vs. 3.10.4

- fork: python
- ref: main
- machine: linux-x86_64
- commit hash: ec9d12b
- commit date: 2024-05-10
- overall geometric mean: 1.17x slower
- HPT reliability: 99.98%
- HPT 99th percentile: 1.02x slower
- Memory change: 1.28x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240510-linux-x86_64-python-main-3.14.0a0-ec9d12b |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| 2to3           | 348 ms                                                 | 395 ms: 1.13x slower                                  |
| chameleon      | 9.68 ms                                                | 12.8 ms: 1.32x slower                                 |
| docutils       | 3.30 sec                                               | 3.38 sec: 1.03x slower                                |
| html5lib       | 88.9 ms                                                | 96.6 ms: 1.09x slower                                 |
| Geometric mean | (ref)                                                  | 1.11x slower                                          |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240510-linux-x86_64-python-main-3.14.0a0-ec9d12b |
|-------------------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| async_tree_io           | 1.77 sec                                               | 938 ms: 1.89x faster                                  |
| async_tree_none         | 728 ms                                                 | 453 ms: 1.61x faster                                  |
| async_tree_memoization  | 870 ms                                                 | 559 ms: 1.56x faster                                  |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 715 ms: 1.42x faster                                  |
| Geometric mean          | (ref)                                                  | 1.61x faster                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240510-linux-x86_64-python-main-3.14.0a0-ec9d12b |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| pidigits       | 191 ms                                                 | 191 ms: 1.00x slower                                  |
| float          | 117 ms                                                 | 133 ms: 1.13x slower                                  |
| nbody          | 154 ms                                                 | 227 ms: 1.48x slower                                  |
| Geometric mean | (ref)                                                  | 1.19x slower                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240510-linux-x86_64-python-main-3.14.0a0-ec9d12b |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| regex_v8       | 27.8 ms                                                | 26.5 ms: 1.05x faster                                 |
| regex_dna      | 227 ms                                                 | 221 ms: 1.02x faster                                  |
| regex_effbot   | 3.63 ms                                                | 3.56 ms: 1.02x faster                                 |
| regex_compile  | 188 ms                                                 | 217 ms: 1.15x slower                                  |
| Geometric mean | (ref)                                                  | 1.01x slower                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240510-linux-x86_64-python-main-3.14.0a0-ec9d12b |
|----------------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| xml_etree_parse      | 168 ms                                                 | 144 ms: 1.17x faster                                  |
| xml_etree_iterparse  | 115 ms                                                 | 113 ms: 1.02x faster                                  |
| json_dumps           | 14.2 ms                                                | 13.9 ms: 1.02x faster                                 |
| json_loads           | 31.2 us                                                | 32.7 us: 1.05x slower                                 |
| pickle_list          | 5.08 us                                                | 5.34 us: 1.05x slower                                 |
| tomli_loads          | 3.14 sec                                               | 3.30 sec: 1.05x slower                                |
| unpickle_list        | 5.20 us                                                | 5.57 us: 1.07x slower                                 |
| xml_etree_generate   | 99.4 ms                                                | 110 ms: 1.10x slower                                  |
| xml_etree_process    | 79.1 ms                                                | 89.6 ms: 1.13x slower                                 |
| pickle               | 10.7 us                                                | 12.4 us: 1.16x slower                                 |
| pickle_pure_python   | 484 us                                                 | 570 us: 1.18x slower                                  |
| unpickle             | 14.4 us                                                | 17.0 us: 1.18x slower                                 |
| unpickle_pure_python | 331 us                                                 | 398 us: 1.20x slower                                  |
| pickle_dict          | 29.6 us                                                | 42.4 us: 1.43x slower                                 |
| Geometric mean       | (ref)                                                  | 1.09x slower                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240510-linux-x86_64-python-main-3.14.0a0-ec9d12b |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 13.3 ms: 1.09x faster                                 |
| python_startup_no_site | 5.93 ms                                                | 9.16 ms: 1.54x slower                                 |
| Geometric mean         | (ref)                                                  | 1.19x slower                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240510-linux-x86_64-python-main-3.14.0a0-ec9d12b |
|-----------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| genshi_xml      | 66.0 ms                                                | 81.4 ms: 1.23x slower                                 |
| genshi_text     | 31.8 ms                                                | 39.4 ms: 1.24x slower                                 |
| django_template | 48.2 ms                                                | 60.1 ms: 1.25x slower                                 |
| mako            | 16.3 ms                                                | 20.7 ms: 1.27x slower                                 |
| Geometric mean  | (ref)                                                  | 1.25x slower                                          |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240510-linux-x86_64-python-main-3.14.0a0-ec9d12b |
|--------------------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| generators               | 80.1 ms                                                | 36.6 ms: 2.19x faster                                 |
| typing_runtime_protocols | 544 us                                                 | 259 us: 2.10x faster                                  |
| async_tree_io            | 1.77 sec                                               | 938 ms: 1.89x faster                                  |
| async_tree_none          | 728 ms                                                 | 453 ms: 1.61x faster                                  |
| asyncio_tcp              | 922 ms                                                 | 590 ms: 1.56x faster                                  |
| async_tree_memoization   | 870 ms                                                 | 559 ms: 1.56x faster                                  |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 715 ms: 1.42x faster                                  |
| pylint                   | 551 ms                                                 | 398 ms: 1.38x faster                                  |
| asyncio_tcp_ssl          | 2.57 sec                                               | 2.14 sec: 1.20x faster                                |
| xml_etree_parse          | 168 ms                                                 | 144 ms: 1.17x faster                                  |
| bench_mp_pool            | 24.0 ms                                                | 21.0 ms: 1.15x faster                                 |
| create_gc_cycles         | 1.62 ms                                                | 1.42 ms: 1.14x faster                                 |
| gc_traversal             | 3.62 ms                                                | 3.21 ms: 1.13x faster                                 |
| crypto_pyaes             | 128 ms                                                 | 115 ms: 1.11x faster                                  |
| python_startup           | 14.6 ms                                                | 13.3 ms: 1.09x faster                                 |
| regex_v8                 | 27.8 ms                                                | 26.5 ms: 1.05x faster                                 |
| coroutines               | 35.1 ms                                                | 33.5 ms: 1.05x faster                                 |
| comprehensions           | 28.8 us                                                | 27.7 us: 1.04x faster                                 |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 6.24 ms: 1.04x faster                                 |
| regex_dna                | 227 ms                                                 | 221 ms: 1.02x faster                                  |
| xml_etree_iterparse      | 115 ms                                                 | 113 ms: 1.02x faster                                  |
| richards                 | 79.3 ms                                                | 77.8 ms: 1.02x faster                                 |
| regex_effbot             | 3.63 ms                                                | 3.56 ms: 1.02x faster                                 |
| json_dumps               | 14.2 ms                                                | 13.9 ms: 1.02x faster                                 |
| richards_super           | 94.7 ms                                                | 93.3 ms: 1.02x faster                                 |
| scimark_fft              | 466 ms                                                 | 461 ms: 1.01x faster                                  |
| pycparser                | 1.58 sec                                               | 1.56 sec: 1.01x faster                                |
| pidigits                 | 191 ms                                                 | 191 ms: 1.00x slower                                  |
| asyncio_websockets       | 559 ms                                                 | 566 ms: 1.01x slower                                  |
| pathlib                  | 20.5 ms                                                | 20.9 ms: 1.02x slower                                 |
| docutils                 | 3.30 sec                                               | 3.38 sec: 1.03x slower                                |
| logging_silent           | 190 ns                                                 | 195 ns: 1.03x slower                                  |
| scimark_monte_carlo      | 118 ms                                                 | 122 ms: 1.03x slower                                  |
| dulwich_log              | 84.3 ms                                                | 87.8 ms: 1.04x slower                                 |
| pyflate                  | 716 ms                                                 | 749 ms: 1.05x slower                                  |
| json_loads               | 31.2 us                                                | 32.7 us: 1.05x slower                                 |
| pickle_list              | 5.08 us                                                | 5.34 us: 1.05x slower                                 |
| tomli_loads              | 3.14 sec                                               | 3.30 sec: 1.05x slower                                |
| deltablue                | 7.91 ms                                                | 8.32 ms: 1.05x slower                                 |
| sqlite_synth             | 3.02 us                                                | 3.21 us: 1.06x slower                                 |
| unpickle_list            | 5.20 us                                                | 5.57 us: 1.07x slower                                 |
| chaos                    | 115 ms                                                 | 124 ms: 1.07x slower                                  |
| json                     | 5.69 ms                                                | 6.13 ms: 1.08x slower                                 |
| html5lib                 | 88.9 ms                                                | 96.6 ms: 1.09x slower                                 |
| xml_etree_generate       | 99.4 ms                                                | 110 ms: 1.10x slower                                  |
| spectral_norm            | 170 ms                                                 | 188 ms: 1.11x slower                                  |
| deepcopy_memo            | 58.5 us                                                | 65.1 us: 1.11x slower                                 |
| nqueens                  | 106 ms                                                 | 118 ms: 1.12x slower                                  |
| sympy_integrate          | 25.8 ms                                                | 29.0 ms: 1.12x slower                                 |
| fannkuch                 | 532 ms                                                 | 600 ms: 1.13x slower                                  |
| xml_etree_process        | 79.1 ms                                                | 89.6 ms: 1.13x slower                                 |
| 2to3                     | 348 ms                                                 | 395 ms: 1.13x slower                                  |
| float                    | 117 ms                                                 | 133 ms: 1.13x slower                                  |
| regex_compile            | 188 ms                                                 | 217 ms: 1.15x slower                                  |
| pickle                   | 10.7 us                                                | 12.4 us: 1.16x slower                                 |
| raytrace                 | 507 ms                                                 | 589 ms: 1.16x slower                                  |
| sqlglot_transpile        | 2.57 ms                                                | 2.99 ms: 1.16x slower                                 |
| sqlglot_parse            | 2.17 ms                                                | 2.52 ms: 1.16x slower                                 |
| pickle_pure_python       | 484 us                                                 | 570 us: 1.18x slower                                  |
| unpickle                 | 14.4 us                                                | 17.0 us: 1.18x slower                                 |
| hexiom                   | 10.4 ms                                                | 12.3 ms: 1.19x slower                                 |
| mdp                      | 2.85 sec                                               | 3.42 sec: 1.20x slower                                |
| unpickle_pure_python     | 331 us                                                 | 398 us: 1.20x slower                                  |
| deepcopy                 | 479 us                                                 | 578 us: 1.21x slower                                  |
| meteor_contest           | 120 ms                                                 | 145 ms: 1.21x slower                                  |
| sqlglot_normalize        | 143 ms                                                 | 174 ms: 1.22x slower                                  |
| scimark_sor              | 220 ms                                                 | 270 ms: 1.23x slower                                  |
| genshi_xml               | 66.0 ms                                                | 81.4 ms: 1.23x slower                                 |
| genshi_text              | 31.8 ms                                                | 39.4 ms: 1.24x slower                                 |
| sympy_str                | 346 ms                                                 | 430 ms: 1.24x slower                                  |
| async_generators         | 444 ms                                                 | 553 ms: 1.25x slower                                  |
| django_template          | 48.2 ms                                                | 60.1 ms: 1.25x slower                                 |
| deepcopy_reduce          | 4.17 us                                                | 5.22 us: 1.25x slower                                 |
| sqlglot_optimize         | 69.2 ms                                                | 87.6 ms: 1.27x slower                                 |
| mako                     | 16.3 ms                                                | 20.7 ms: 1.27x slower                                 |
| logging_simple           | 8.30 us                                                | 10.5 us: 1.27x slower                                 |
| pprint_pformat           | 2.10 sec                                               | 2.70 sec: 1.29x slower                                |
| pprint_safe_repr         | 1.02 sec                                               | 1.31 sec: 1.29x slower                                |
| go                       | 240 ms                                                 | 311 ms: 1.29x slower                                  |
| logging_format           | 9.09 us                                                | 11.8 us: 1.30x slower                                 |
| sympy_sum                | 196 ms                                                 | 258 ms: 1.31x slower                                  |
| chameleon                | 9.68 ms                                                | 12.8 ms: 1.32x slower                                 |
| sympy_expand             | 566 ms                                                 | 758 ms: 1.34x slower                                  |
| scimark_lu               | 176 ms                                                 | 238 ms: 1.35x slower                                  |
| pickle_dict              | 29.6 us                                                | 42.4 us: 1.43x slower                                 |
| nbody                    | 154 ms                                                 | 227 ms: 1.48x slower                                  |
| python_startup_no_site   | 5.93 ms                                                | 9.16 ms: 1.54x slower                                 |
| flaskblogging            | 8.58 ms                                                | 13.4 ms: 1.56x slower                                 |
| bench_thread_pool        | 986 us                                                 | 3.04 ms: 3.09x slower                                 |
| coverage                 | 79.4 ms                                                | 787 ms: 9.91x slower                                  |
| thrift                   | 1.07 ms                                                | 13.1 ms: 12.19x slower                                |
| telco                    | 7.27 ms                                                | 317 ms: 43.59x slower                                 |
| Geometric mean           | (ref)                                                  | 1.17x slower                                          |

Benchmark hidden because not significant (1): tornado_http
Ignored benchmarks (8) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, dask, djangocms, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
Ignored benchmarks (4) of results/bm-20240510-3.14.0a0-ec9d12b-NOGIL/bm-20240510-linux-x86_64-python-main-3.14.0a0-ec9d12b.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg

# HPT report

- Reliability score: 99.98% likely to be slow
- 90% likely to have a slowdown of 1.05x
- 95% likely to have a slowdown of 1.04x
- 99% likely to have a slowdown of 1.02x

# Memory
- memory change: 1.28x