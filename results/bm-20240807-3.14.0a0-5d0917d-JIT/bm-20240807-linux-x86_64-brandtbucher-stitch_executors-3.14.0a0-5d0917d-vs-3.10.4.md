# Results vs. 3.10.4

- fork: brandtbucher
- ref: stitch_executors
- machine: linux-x86_64
- commit hash: 5d0917d
- commit date: 2024-08-07
- overall geometric mean: 1.43x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.27x faster
- Memory change: 1.19x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240807-linux-x86_64-brandtbucher-stitch_executors-3.14.0a0-5d0917d |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 273 ms: 1.28x faster                                                    |
| docutils       | 3.30 sec                                               | 2.96 sec: 1.12x faster                                                  |
| html5lib       | 88.9 ms                                                | 65.8 ms: 1.35x faster                                                   |
| tornado_http   | 136 ms                                                 | 95.6 ms: 1.43x faster                                                   |
| Geometric mean | (ref)                                                  | 1.29x faster                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240807-linux-x86_64-brandtbucher-stitch_executors-3.14.0a0-5d0917d |
|-------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_none         | 728 ms                                                 | 328 ms: 2.22x faster                                                    |
| async_tree_memoization  | 870 ms                                                 | 422 ms: 2.06x faster                                                    |
| async_tree_io           | 1.77 sec                                               | 911 ms: 1.94x faster                                                    |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 568 ms: 1.79x faster                                                    |
| Geometric mean          | (ref)                                                  | 2.00x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240807-linux-x86_64-brandtbucher-stitch_executors-3.14.0a0-5d0917d |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 79.7 ms: 1.93x faster                                                   |
| float          | 117 ms                                                 | 71.8 ms: 1.63x faster                                                   |
| pidigits       | 191 ms                                                 | 186 ms: 1.03x faster                                                    |
| Geometric mean | (ref)                                                  | 1.48x faster                                                            |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240807-linux-x86_64-brandtbucher-stitch_executors-3.14.0a0-5d0917d |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 135 ms: 1.40x faster                                                    |
| regex_v8       | 27.8 ms                                                | 25.7 ms: 1.08x faster                                                   |
| regex_dna      | 227 ms                                                 | 232 ms: 1.02x slower                                                    |
| regex_effbot   | 3.63 ms                                                | 3.87 ms: 1.07x slower                                                   |
| Geometric mean | (ref)                                                  | 1.09x faster                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240807-linux-x86_64-brandtbucher-stitch_executors-3.14.0a0-5d0917d |
|----------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| pickle_pure_python   | 484 us                                                 | 299 us: 1.62x faster                                                    |
| tomli_loads          | 3.14 sec                                               | 1.95 sec: 1.61x faster                                                  |
| unpickle_pure_python | 331 us                                                 | 213 us: 1.55x faster                                                    |
| xml_etree_process    | 79.1 ms                                                | 56.6 ms: 1.40x faster                                                   |
| json_dumps           | 14.2 ms                                                | 10.3 ms: 1.37x faster                                                   |
| xml_etree_generate   | 99.4 ms                                                | 79.8 ms: 1.25x faster                                                   |
| xml_etree_iterparse  | 115 ms                                                 | 99.7 ms: 1.16x faster                                                   |
| xml_etree_parse      | 168 ms                                                 | 148 ms: 1.13x faster                                                    |
| json_loads           | 31.2 us                                                | 27.7 us: 1.13x faster                                                   |
| Geometric mean       | (ref)                                                  | 1.34x faster                                                            |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240807-linux-x86_64-brandtbucher-stitch_executors-3.14.0a0-5d0917d |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 10.6 ms: 1.37x faster                                                   |
| python_startup_no_site | 5.93 ms                                                | 7.20 ms: 1.21x slower                                                   |
| Geometric mean         | (ref)                                                  | 1.06x faster                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240807-linux-x86_64-brandtbucher-stitch_executors-3.14.0a0-5d0917d |
|-----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mako            | 16.3 ms                                                | 9.69 ms: 1.68x faster                                                   |
| django_template | 48.2 ms                                                | 36.2 ms: 1.33x faster                                                   |
| genshi_text     | 31.8 ms                                                | 25.0 ms: 1.27x faster                                                   |
| genshi_xml      | 66.0 ms                                                | 56.1 ms: 1.18x faster                                                   |
| Geometric mean  | (ref)                                                  | 1.35x faster                                                            |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240807-linux-x86_64-brandtbucher-stitch_executors-3.14.0a0-5d0917d |
|--------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 173 us: 3.14x faster                                                    |
| generators               | 80.1 ms                                                | 32.9 ms: 2.44x faster                                                   |
| async_tree_none          | 728 ms                                                 | 328 ms: 2.22x faster                                                    |
| deltablue                | 7.91 ms                                                | 3.56 ms: 2.22x faster                                                   |
| deepcopy_memo            | 58.5 us                                                | 28.3 us: 2.07x faster                                                   |
| async_tree_memoization   | 870 ms                                                 | 422 ms: 2.06x faster                                                    |
| chaos                    | 115 ms                                                 | 57.7 ms: 2.00x faster                                                   |
| richards_super           | 94.7 ms                                                | 47.5 ms: 2.00x faster                                                   |
| async_tree_io            | 1.77 sec                                               | 911 ms: 1.94x faster                                                    |
| scimark_monte_carlo      | 118 ms                                                 | 60.9 ms: 1.94x faster                                                   |
| crypto_pyaes             | 128 ms                                                 | 66.1 ms: 1.93x faster                                                   |
| nbody                    | 154 ms                                                 | 79.7 ms: 1.93x faster                                                   |
| richards                 | 79.3 ms                                                | 41.5 ms: 1.91x faster                                                   |
| scimark_sor              | 220 ms                                                 | 115 ms: 1.91x faster                                                    |
| raytrace                 | 507 ms                                                 | 267 ms: 1.90x faster                                                    |
| logging_silent           | 190 ns                                                 | 103 ns: 1.85x faster                                                    |
| asyncio_tcp              | 922 ms                                                 | 502 ms: 1.84x faster                                                    |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 568 ms: 1.79x faster                                                    |
| deepcopy                 | 479 us                                                 | 270 us: 1.77x faster                                                    |
| comprehensions           | 28.8 us                                                | 16.6 us: 1.74x faster                                                   |
| sqlglot_parse            | 2.17 ms                                                | 1.27 ms: 1.71x faster                                                   |
| mako                     | 16.3 ms                                                | 9.69 ms: 1.68x faster                                                   |
| spectral_norm            | 170 ms                                                 | 101 ms: 1.68x faster                                                    |
| scimark_lu               | 176 ms                                                 | 106 ms: 1.67x faster                                                    |
| go                       | 240 ms                                                 | 145 ms: 1.66x faster                                                    |
| float                    | 117 ms                                                 | 71.8 ms: 1.63x faster                                                   |
| pickle_pure_python       | 484 us                                                 | 299 us: 1.62x faster                                                    |
| hexiom                   | 10.4 ms                                                | 6.44 ms: 1.61x faster                                                   |
| tomli_loads              | 3.14 sec                                               | 1.95 sec: 1.61x faster                                                  |
| sqlglot_transpile        | 2.57 ms                                                | 1.60 ms: 1.60x faster                                                   |
| pyflate                  | 716 ms                                                 | 448 ms: 1.60x faster                                                    |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.14 ms: 1.56x faster                                                   |
| coroutines               | 35.1 ms                                                | 22.6 ms: 1.55x faster                                                   |
| scimark_fft              | 466 ms                                                 | 300 ms: 1.55x faster                                                    |
| unpickle_pure_python     | 331 us                                                 | 213 us: 1.55x faster                                                    |
| pylint                   | 551 ms                                                 | 358 ms: 1.54x faster                                                    |
| deepcopy_reduce          | 4.17 us                                                | 2.77 us: 1.50x faster                                                   |
| logging_simple           | 8.30 us                                                | 5.53 us: 1.50x faster                                                   |
| logging_format           | 9.09 us                                                | 6.07 us: 1.50x faster                                                   |
| pprint_pformat           | 2.10 sec                                               | 1.45 sec: 1.45x faster                                                  |
| fannkuch                 | 532 ms                                                 | 370 ms: 1.44x faster                                                    |
| tornado_http             | 136 ms                                                 | 95.6 ms: 1.43x faster                                                   |
| asyncio_tcp_ssl          | 2.57 sec                                               | 1.81 sec: 1.42x faster                                                  |
| pprint_safe_repr         | 1.02 sec                                               | 718 ms: 1.42x faster                                                    |
| regex_compile            | 188 ms                                                 | 135 ms: 1.40x faster                                                    |
| xml_etree_process        | 79.1 ms                                                | 56.6 ms: 1.40x faster                                                   |
| json_dumps               | 14.2 ms                                                | 10.3 ms: 1.37x faster                                                   |
| python_startup           | 14.6 ms                                                | 10.6 ms: 1.37x faster                                                   |
| html5lib                 | 88.9 ms                                                | 65.8 ms: 1.35x faster                                                   |
| thrift                   | 1.07 ms                                                | 802 us: 1.34x faster                                                    |
| django_template          | 48.2 ms                                                | 36.2 ms: 1.33x faster                                                   |
| pycparser                | 1.58 sec                                               | 1.19 sec: 1.32x faster                                                  |
| pathlib                  | 20.5 ms                                                | 16.0 ms: 1.28x faster                                                   |
| 2to3                     | 348 ms                                                 | 273 ms: 1.28x faster                                                    |
| sqlglot_normalize        | 143 ms                                                 | 112 ms: 1.27x faster                                                    |
| genshi_text              | 31.8 ms                                                | 25.0 ms: 1.27x faster                                                   |
| nqueens                  | 106 ms                                                 | 83.9 ms: 1.26x faster                                                   |
| xml_etree_generate       | 99.4 ms                                                | 79.8 ms: 1.25x faster                                                   |
| sqlglot_optimize         | 69.2 ms                                                | 56.4 ms: 1.23x faster                                                   |
| bench_thread_pool        | 986 us                                                 | 829 us: 1.19x faster                                                    |
| genshi_xml               | 66.0 ms                                                | 56.1 ms: 1.18x faster                                                   |
| xml_etree_iterparse      | 115 ms                                                 | 99.7 ms: 1.16x faster                                                   |
| meteor_contest           | 120 ms                                                 | 105 ms: 1.14x faster                                                    |
| sympy_str                | 346 ms                                                 | 305 ms: 1.13x faster                                                    |
| sympy_integrate          | 25.8 ms                                                | 22.8 ms: 1.13x faster                                                   |
| xml_etree_parse          | 168 ms                                                 | 148 ms: 1.13x faster                                                    |
| sympy_sum                | 196 ms                                                 | 174 ms: 1.13x faster                                                    |
| json_loads               | 31.2 us                                                | 27.7 us: 1.13x faster                                                   |
| docutils                 | 3.30 sec                                               | 2.96 sec: 1.12x faster                                                  |
| mdp                      | 2.85 sec                                               | 2.56 sec: 1.11x faster                                                  |
| sympy_expand             | 566 ms                                                 | 517 ms: 1.09x faster                                                    |
| json                     | 5.69 ms                                                | 5.20 ms: 1.09x faster                                                   |
| regex_v8                 | 27.8 ms                                                | 25.7 ms: 1.08x faster                                                   |
| pidigits                 | 191 ms                                                 | 186 ms: 1.03x faster                                                    |
| regex_dna                | 227 ms                                                 | 232 ms: 1.02x slower                                                    |
| async_generators         | 444 ms                                                 | 458 ms: 1.03x slower                                                    |
| gc_traversal             | 3.62 ms                                                | 3.75 ms: 1.03x slower                                                   |
| regex_effbot             | 3.63 ms                                                | 3.87 ms: 1.07x slower                                                   |
| telco                    | 7.27 ms                                                | 7.87 ms: 1.08x slower                                                   |
| create_gc_cycles         | 1.62 ms                                                | 1.77 ms: 1.09x slower                                                   |
| coverage                 | 79.4 ms                                                | 90.8 ms: 1.14x slower                                                   |
| python_startup_no_site   | 5.93 ms                                                | 7.20 ms: 1.21x slower                                                   |
| Geometric mean           | (ref)                                                  | 1.43x faster                                                            |

Benchmark hidden because not significant (2): asyncio_websockets, bench_mp_pool
Ignored benchmarks (17) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, djangocms, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (5) of results/bm-20240807-3.14.0a0-5d0917d-JIT/bm-20240807-linux-x86_64-brandtbucher-stitch_executors-3.14.0a0-5d0917d.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.32x
- 95% likely to have a speedup of 1.29x
- 99% likely to have a speedup of 1.27x

# Memory
- memory change: 1.19x