# Results vs. 3.10.4

- fork: brandtbucher
- ref: no_progress_needed
- machine: linux-x86_64
- commit hash: 363fca1
- commit date: 2024-07-13
- overall geometric mean: 1.33x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.19x faster
- Memory change: 1.22x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240713-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-363fca1 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 290 ms: 1.20x faster                                                      |
| docutils       | 3.30 sec                                               | 7.91 sec: 2.40x slower                                                    |
| html5lib       | 88.9 ms                                                | 76.3 ms: 1.16x faster                                                     |
| tornado_http   | 136 ms                                                 | 95.1 ms: 1.43x faster                                                     |
| Geometric mean | (ref)                                                  | 1.05x slower                                                              |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240713-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-363fca1 |
|-------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| async_tree_none         | 728 ms                                                 | 327 ms: 2.23x faster                                                      |
| async_tree_memoization  | 870 ms                                                 | 411 ms: 2.12x faster                                                      |
| async_tree_io           | 1.77 sec                                               | 850 ms: 2.08x faster                                                      |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 563 ms: 1.81x faster                                                      |
| Geometric mean          | (ref)                                                  | 2.05x faster                                                              |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240713-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-363fca1 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 79.8 ms: 1.92x faster                                                     |
| float          | 117 ms                                                 | 70.5 ms: 1.66x faster                                                     |
| pidigits       | 191 ms                                                 | 188 ms: 1.02x faster                                                      |
| Geometric mean | (ref)                                                  | 1.48x faster                                                              |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240713-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-363fca1 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 135 ms: 1.39x faster                                                      |
| regex_v8       | 27.8 ms                                                | 25.4 ms: 1.09x faster                                                     |
| regex_dna      | 227 ms                                                 | 224 ms: 1.01x faster                                                      |
| regex_effbot   | 3.63 ms                                                | 3.86 ms: 1.06x slower                                                     |
| Geometric mean | (ref)                                                  | 1.10x faster                                                              |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240713-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-363fca1 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| tomli_loads          | 3.14 sec                                               | 1.90 sec: 1.65x faster                                                    |
| unpickle_pure_python | 331 us                                                 | 213 us: 1.55x faster                                                      |
| pickle_pure_python   | 484 us                                                 | 313 us: 1.55x faster                                                      |
| json_dumps           | 14.2 ms                                                | 10.5 ms: 1.35x faster                                                     |
| xml_etree_process    | 79.1 ms                                                | 59.8 ms: 1.32x faster                                                     |
| xml_etree_generate   | 99.4 ms                                                | 84.4 ms: 1.18x faster                                                     |
| xml_etree_iterparse  | 115 ms                                                 | 99.3 ms: 1.16x faster                                                     |
| json_loads           | 31.2 us                                                | 27.6 us: 1.13x faster                                                     |
| xml_etree_parse      | 168 ms                                                 | 150 ms: 1.12x faster                                                      |
| Geometric mean       | (ref)                                                  | 1.32x faster                                                              |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240713-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-363fca1 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 10.5 ms: 1.39x faster                                                     |
| python_startup_no_site | 5.93 ms                                                | 7.08 ms: 1.19x slower                                                     |
| Geometric mean         | (ref)                                                  | 1.08x faster                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240713-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-363fca1 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| mako            | 16.3 ms                                                | 9.81 ms: 1.66x faster                                                     |
| django_template | 48.2 ms                                                | 38.6 ms: 1.25x faster                                                     |
| genshi_text     | 31.8 ms                                                | 34.1 ms: 1.07x slower                                                     |
| genshi_xml      | 66.0 ms                                                | 75.1 ms: 1.14x slower                                                     |
| Geometric mean  | (ref)                                                  | 1.14x faster                                                              |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240713-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-363fca1 |
|--------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 172 us: 3.17x faster                                                      |
| generators               | 80.1 ms                                                | 30.2 ms: 2.65x faster                                                     |
| async_tree_none          | 728 ms                                                 | 327 ms: 2.23x faster                                                      |
| deepcopy_memo            | 58.5 us                                                | 26.9 us: 2.18x faster                                                     |
| async_tree_memoization   | 870 ms                                                 | 411 ms: 2.12x faster                                                      |
| richards_super           | 94.7 ms                                                | 45.5 ms: 2.08x faster                                                     |
| async_tree_io            | 1.77 sec                                               | 850 ms: 2.08x faster                                                      |
| richards                 | 79.3 ms                                                | 39.3 ms: 2.02x faster                                                     |
| deltablue                | 7.91 ms                                                | 3.94 ms: 2.01x faster                                                     |
| chaos                    | 115 ms                                                 | 57.9 ms: 1.99x faster                                                     |
| nbody                    | 154 ms                                                 | 79.8 ms: 1.92x faster                                                     |
| crypto_pyaes             | 128 ms                                                 | 67.4 ms: 1.90x faster                                                     |
| scimark_monte_carlo      | 118 ms                                                 | 62.7 ms: 1.89x faster                                                     |
| logging_silent           | 190 ns                                                 | 102 ns: 1.86x faster                                                      |
| asyncio_tcp              | 922 ms                                                 | 503 ms: 1.83x faster                                                      |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 563 ms: 1.81x faster                                                      |
| deepcopy                 | 479 us                                                 | 270 us: 1.78x faster                                                      |
| comprehensions           | 28.8 us                                                | 16.7 us: 1.72x faster                                                     |
| scimark_sor              | 220 ms                                                 | 129 ms: 1.70x faster                                                      |
| spectral_norm            | 170 ms                                                 | 101 ms: 1.69x faster                                                      |
| mako                     | 16.3 ms                                                | 9.81 ms: 1.66x faster                                                     |
| float                    | 117 ms                                                 | 70.5 ms: 1.66x faster                                                     |
| tomli_loads              | 3.14 sec                                               | 1.90 sec: 1.65x faster                                                    |
| go                       | 240 ms                                                 | 147 ms: 1.63x faster                                                      |
| sqlglot_parse            | 2.17 ms                                                | 1.34 ms: 1.62x faster                                                     |
| pyflate                  | 716 ms                                                 | 452 ms: 1.59x faster                                                      |
| hexiom                   | 10.4 ms                                                | 6.67 ms: 1.56x faster                                                     |
| unpickle_pure_python     | 331 us                                                 | 213 us: 1.55x faster                                                      |
| pickle_pure_python       | 484 us                                                 | 313 us: 1.55x faster                                                      |
| deepcopy_reduce          | 4.17 us                                                | 2.69 us: 1.55x faster                                                     |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.20 ms: 1.54x faster                                                     |
| sqlglot_transpile        | 2.57 ms                                                | 1.68 ms: 1.53x faster                                                     |
| logging_simple           | 8.30 us                                                | 5.47 us: 1.52x faster                                                     |
| coroutines               | 35.1 ms                                                | 23.2 ms: 1.51x faster                                                     |
| scimark_lu               | 176 ms                                                 | 117 ms: 1.51x faster                                                      |
| scimark_fft              | 466 ms                                                 | 309 ms: 1.51x faster                                                      |
| logging_format           | 9.09 us                                                | 6.06 us: 1.50x faster                                                     |
| fannkuch                 | 532 ms                                                 | 367 ms: 1.45x faster                                                      |
| tornado_http             | 136 ms                                                 | 95.1 ms: 1.43x faster                                                     |
| asyncio_tcp_ssl          | 2.57 sec                                               | 1.81 sec: 1.42x faster                                                    |
| pylint                   | 551 ms                                                 | 390 ms: 1.41x faster                                                      |
| python_startup           | 14.6 ms                                                | 10.5 ms: 1.39x faster                                                     |
| regex_compile            | 188 ms                                                 | 135 ms: 1.39x faster                                                      |
| pprint_pformat           | 2.10 sec                                               | 1.51 sec: 1.39x faster                                                    |
| pprint_safe_repr         | 1.02 sec                                               | 735 ms: 1.39x faster                                                      |
| json_dumps               | 14.2 ms                                                | 10.5 ms: 1.35x faster                                                     |
| pycparser                | 1.58 sec                                               | 1.17 sec: 1.35x faster                                                    |
| thrift                   | 1.07 ms                                                | 797 us: 1.34x faster                                                      |
| xml_etree_process        | 79.1 ms                                                | 59.8 ms: 1.32x faster                                                     |
| sqlglot_normalize        | 143 ms                                                 | 112 ms: 1.28x faster                                                      |
| pathlib                  | 20.5 ms                                                | 16.1 ms: 1.27x faster                                                     |
| dulwich_log              | 84.3 ms                                                | 67.3 ms: 1.25x faster                                                     |
| django_template          | 48.2 ms                                                | 38.6 ms: 1.25x faster                                                     |
| 2to3                     | 348 ms                                                 | 290 ms: 1.20x faster                                                      |
| dask                     | 441 ms                                                 | 369 ms: 1.19x faster                                                      |
| sympy_sum                | 196 ms                                                 | 166 ms: 1.19x faster                                                      |
| xml_etree_generate       | 99.4 ms                                                | 84.4 ms: 1.18x faster                                                     |
| sqlglot_optimize         | 69.2 ms                                                | 58.9 ms: 1.17x faster                                                     |
| html5lib                 | 88.9 ms                                                | 76.3 ms: 1.16x faster                                                     |
| xml_etree_iterparse      | 115 ms                                                 | 99.3 ms: 1.16x faster                                                     |
| nqueens                  | 106 ms                                                 | 91.4 ms: 1.16x faster                                                     |
| sympy_str                | 346 ms                                                 | 300 ms: 1.15x faster                                                      |
| sympy_expand             | 566 ms                                                 | 497 ms: 1.14x faster                                                      |
| json_loads               | 31.2 us                                                | 27.6 us: 1.13x faster                                                     |
| xml_etree_parse          | 168 ms                                                 | 150 ms: 1.12x faster                                                      |
| json                     | 5.69 ms                                                | 5.11 ms: 1.11x faster                                                     |
| meteor_contest           | 120 ms                                                 | 109 ms: 1.10x faster                                                      |
| regex_v8                 | 27.8 ms                                                | 25.4 ms: 1.09x faster                                                     |
| sympy_integrate          | 25.8 ms                                                | 24.5 ms: 1.05x faster                                                     |
| mdp                      | 2.85 sec                                               | 2.73 sec: 1.04x faster                                                    |
| bench_thread_pool        | 986 us                                                 | 958 us: 1.03x faster                                                      |
| gc_traversal             | 3.62 ms                                                | 3.55 ms: 1.02x faster                                                     |
| pidigits                 | 191 ms                                                 | 188 ms: 1.02x faster                                                      |
| regex_dna                | 227 ms                                                 | 224 ms: 1.01x faster                                                      |
| async_generators         | 444 ms                                                 | 456 ms: 1.03x slower                                                      |
| regex_effbot             | 3.63 ms                                                | 3.86 ms: 1.06x slower                                                     |
| genshi_text              | 31.8 ms                                                | 34.1 ms: 1.07x slower                                                     |
| create_gc_cycles         | 1.62 ms                                                | 1.75 ms: 1.08x slower                                                     |
| telco                    | 7.27 ms                                                | 7.99 ms: 1.10x slower                                                     |
| genshi_xml               | 66.0 ms                                                | 75.1 ms: 1.14x slower                                                     |
| coverage                 | 79.4 ms                                                | 93.4 ms: 1.18x slower                                                     |
| python_startup_no_site   | 5.93 ms                                                | 7.08 ms: 1.19x slower                                                     |
| docutils                 | 3.30 sec                                               | 7.91 sec: 2.40x slower                                                    |
| raytrace                 | 507 ms                                                 | 5.99 sec: 11.83x slower                                                   |
| Geometric mean           | (ref)                                                  | 1.33x faster                                                              |

Benchmark hidden because not significant (2): asyncio_websockets, bench_mp_pool
Ignored benchmarks (15) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (5) of results/bm-20240713-3.14.0a0-363fca1-JIT/bm-20240713-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-363fca1.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.26x
- 95% likely to have a speedup of 1.23x
- 99% likely to have a speedup of 1.19x

# Memory
- memory change: 1.22x