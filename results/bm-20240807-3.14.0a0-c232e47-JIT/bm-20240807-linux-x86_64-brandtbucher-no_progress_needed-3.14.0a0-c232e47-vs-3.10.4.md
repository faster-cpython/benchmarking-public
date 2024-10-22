# Results vs. 3.10.4

- fork: brandtbucher
- ref: no_progress_needed
- machine: linux-x86_64
- commit hash: c232e47
- commit date: 2024-08-07
- overall geometric mean: 1.35x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.21x faster
- Memory change: 1.23x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240807-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-c232e47 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 282 ms: 1.23x faster                                                      |
| docutils       | 3.30 sec                                               | 6.89 sec: 2.09x slower                                                    |
| html5lib       | 88.9 ms                                                | 67.4 ms: 1.32x faster                                                     |
| tornado_http   | 136 ms                                                 | 93.1 ms: 1.46x faster                                                     |
| Geometric mean | (ref)                                                  | 1.03x faster                                                              |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240807-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-c232e47 |
|-------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| async_tree_none         | 728 ms                                                 | 331 ms: 2.20x faster                                                      |
| async_tree_memoization  | 870 ms                                                 | 432 ms: 2.01x faster                                                      |
| async_tree_io           | 1.77 sec                                               | 914 ms: 1.93x faster                                                      |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 571 ms: 1.78x faster                                                      |
| Geometric mean          | (ref)                                                  | 1.98x faster                                                              |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240807-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-c232e47 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 79.4 ms: 1.93x faster                                                     |
| float          | 117 ms                                                 | 71.0 ms: 1.65x faster                                                     |
| pidigits       | 191 ms                                                 | 186 ms: 1.03x faster                                                      |
| Geometric mean | (ref)                                                  | 1.49x faster                                                              |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240807-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-c232e47 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 136 ms: 1.39x faster                                                      |
| regex_v8       | 27.8 ms                                                | 24.7 ms: 1.13x faster                                                     |
| regex_dna      | 227 ms                                                 | 224 ms: 1.01x faster                                                      |
| regex_effbot   | 3.63 ms                                                | 3.82 ms: 1.05x slower                                                     |
| Geometric mean | (ref)                                                  | 1.11x faster                                                              |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240807-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-c232e47 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| tomli_loads          | 3.14 sec                                               | 1.89 sec: 1.66x faster                                                    |
| unpickle_pure_python | 331 us                                                 | 211 us: 1.57x faster                                                      |
| pickle_pure_python   | 484 us                                                 | 316 us: 1.53x faster                                                      |
| json_dumps           | 14.2 ms                                                | 10.2 ms: 1.38x faster                                                     |
| xml_etree_process    | 79.1 ms                                                | 57.8 ms: 1.37x faster                                                     |
| xml_etree_generate   | 99.4 ms                                                | 84.1 ms: 1.18x faster                                                     |
| xml_etree_iterparse  | 115 ms                                                 | 99.6 ms: 1.16x faster                                                     |
| xml_etree_parse      | 168 ms                                                 | 147 ms: 1.14x faster                                                      |
| json_loads           | 31.2 us                                                | 28.0 us: 1.11x faster                                                     |
| Geometric mean       | (ref)                                                  | 1.33x faster                                                              |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240807-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-c232e47 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 10.6 ms: 1.37x faster                                                     |
| python_startup_no_site | 5.93 ms                                                | 7.20 ms: 1.21x slower                                                     |
| Geometric mean         | (ref)                                                  | 1.06x faster                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240807-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-c232e47 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| mako            | 16.3 ms                                                | 9.71 ms: 1.68x faster                                                     |
| django_template | 48.2 ms                                                | 35.3 ms: 1.36x faster                                                     |
| genshi_text     | 31.8 ms                                                | 25.5 ms: 1.25x faster                                                     |
| genshi_xml      | 66.0 ms                                                | 57.1 ms: 1.16x faster                                                     |
| Geometric mean  | (ref)                                                  | 1.35x faster                                                              |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240807-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-c232e47 |
|--------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 170 us: 3.19x faster                                                      |
| deltablue                | 7.91 ms                                                | 3.06 ms: 2.58x faster                                                     |
| generators               | 80.1 ms                                                | 32.8 ms: 2.44x faster                                                     |
| async_tree_none          | 728 ms                                                 | 331 ms: 2.20x faster                                                      |
| deepcopy_memo            | 58.5 us                                                | 27.5 us: 2.13x faster                                                     |
| richards_super           | 94.7 ms                                                | 45.4 ms: 2.09x faster                                                     |
| async_tree_memoization   | 870 ms                                                 | 432 ms: 2.01x faster                                                      |
| richards                 | 79.3 ms                                                | 39.7 ms: 2.00x faster                                                     |
| chaos                    | 115 ms                                                 | 58.1 ms: 1.99x faster                                                     |
| async_tree_io            | 1.77 sec                                               | 914 ms: 1.93x faster                                                      |
| crypto_pyaes             | 128 ms                                                 | 66.1 ms: 1.93x faster                                                     |
| nbody                    | 154 ms                                                 | 79.4 ms: 1.93x faster                                                     |
| logging_silent           | 190 ns                                                 | 99.8 ns: 1.90x faster                                                     |
| scimark_sor              | 220 ms                                                 | 116 ms: 1.90x faster                                                      |
| scimark_monte_carlo      | 118 ms                                                 | 62.8 ms: 1.88x faster                                                     |
| deepcopy                 | 479 us                                                 | 260 us: 1.85x faster                                                      |
| asyncio_tcp              | 922 ms                                                 | 502 ms: 1.84x faster                                                      |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 571 ms: 1.78x faster                                                      |
| comprehensions           | 28.8 us                                                | 16.4 us: 1.76x faster                                                     |
| spectral_norm            | 170 ms                                                 | 99.5 ms: 1.71x faster                                                     |
| mako                     | 16.3 ms                                                | 9.71 ms: 1.68x faster                                                     |
| tomli_loads              | 3.14 sec                                               | 1.89 sec: 1.66x faster                                                    |
| go                       | 240 ms                                                 | 144 ms: 1.66x faster                                                      |
| float                    | 117 ms                                                 | 71.0 ms: 1.65x faster                                                     |
| scimark_lu               | 176 ms                                                 | 107 ms: 1.64x faster                                                      |
| pyflate                  | 716 ms                                                 | 445 ms: 1.61x faster                                                      |
| unpickle_pure_python     | 331 us                                                 | 211 us: 1.57x faster                                                      |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.15 ms: 1.56x faster                                                     |
| deepcopy_reduce          | 4.17 us                                                | 2.68 us: 1.55x faster                                                     |
| coroutines               | 35.1 ms                                                | 22.6 ms: 1.55x faster                                                     |
| hexiom                   | 10.4 ms                                                | 6.71 ms: 1.55x faster                                                     |
| sqlglot_parse            | 2.17 ms                                                | 1.40 ms: 1.54x faster                                                     |
| pickle_pure_python       | 484 us                                                 | 316 us: 1.53x faster                                                      |
| scimark_fft              | 466 ms                                                 | 304 ms: 1.53x faster                                                      |
| logging_simple           | 8.30 us                                                | 5.47 us: 1.52x faster                                                     |
| logging_format           | 9.09 us                                                | 6.01 us: 1.51x faster                                                     |
| sqlglot_transpile        | 2.57 ms                                                | 1.73 ms: 1.49x faster                                                     |
| tornado_http             | 136 ms                                                 | 93.1 ms: 1.46x faster                                                     |
| fannkuch                 | 532 ms                                                 | 372 ms: 1.43x faster                                                      |
| asyncio_tcp_ssl          | 2.57 sec                                               | 1.81 sec: 1.42x faster                                                    |
| pprint_safe_repr         | 1.02 sec                                               | 733 ms: 1.39x faster                                                      |
| regex_compile            | 188 ms                                                 | 136 ms: 1.39x faster                                                      |
| json_dumps               | 14.2 ms                                                | 10.2 ms: 1.38x faster                                                     |
| python_startup           | 14.6 ms                                                | 10.6 ms: 1.37x faster                                                     |
| xml_etree_process        | 79.1 ms                                                | 57.8 ms: 1.37x faster                                                     |
| pprint_pformat           | 2.10 sec                                               | 1.54 sec: 1.37x faster                                                    |
| django_template          | 48.2 ms                                                | 35.3 ms: 1.36x faster                                                     |
| thrift                   | 1.07 ms                                                | 798 us: 1.34x faster                                                      |
| html5lib                 | 88.9 ms                                                | 67.4 ms: 1.32x faster                                                     |
| pathlib                  | 20.5 ms                                                | 16.0 ms: 1.28x faster                                                     |
| sqlglot_normalize        | 143 ms                                                 | 113 ms: 1.27x faster                                                      |
| genshi_text              | 31.8 ms                                                | 25.5 ms: 1.25x faster                                                     |
| pylint                   | 551 ms                                                 | 443 ms: 1.25x faster                                                      |
| 2to3                     | 348 ms                                                 | 282 ms: 1.23x faster                                                      |
| nqueens                  | 106 ms                                                 | 86.3 ms: 1.23x faster                                                     |
| bench_thread_pool        | 986 us                                                 | 817 us: 1.21x faster                                                      |
| xml_etree_generate       | 99.4 ms                                                | 84.1 ms: 1.18x faster                                                     |
| sympy_str                | 346 ms                                                 | 296 ms: 1.17x faster                                                      |
| xml_etree_iterparse      | 115 ms                                                 | 99.6 ms: 1.16x faster                                                     |
| genshi_xml               | 66.0 ms                                                | 57.1 ms: 1.16x faster                                                     |
| sympy_sum                | 196 ms                                                 | 171 ms: 1.15x faster                                                      |
| sympy_expand             | 566 ms                                                 | 496 ms: 1.14x faster                                                      |
| sqlglot_optimize         | 69.2 ms                                                | 60.6 ms: 1.14x faster                                                     |
| xml_etree_parse          | 168 ms                                                 | 147 ms: 1.14x faster                                                      |
| sympy_integrate          | 25.8 ms                                                | 22.8 ms: 1.13x faster                                                     |
| meteor_contest           | 120 ms                                                 | 106 ms: 1.13x faster                                                      |
| regex_v8                 | 27.8 ms                                                | 24.7 ms: 1.13x faster                                                     |
| json                     | 5.69 ms                                                | 5.08 ms: 1.12x faster                                                     |
| json_loads               | 31.2 us                                                | 28.0 us: 1.11x faster                                                     |
| mdp                      | 2.85 sec                                               | 2.70 sec: 1.06x faster                                                    |
| pidigits                 | 191 ms                                                 | 186 ms: 1.03x faster                                                      |
| regex_dna                | 227 ms                                                 | 224 ms: 1.01x faster                                                      |
| asyncio_websockets       | 559 ms                                                 | 556 ms: 1.01x faster                                                      |
| async_generators         | 444 ms                                                 | 454 ms: 1.02x slower                                                      |
| gc_traversal             | 3.62 ms                                                | 3.75 ms: 1.03x slower                                                     |
| pycparser                | 1.58 sec                                               | 1.64 sec: 1.04x slower                                                    |
| regex_effbot             | 3.63 ms                                                | 3.82 ms: 1.05x slower                                                     |
| telco                    | 7.27 ms                                                | 7.83 ms: 1.08x slower                                                     |
| create_gc_cycles         | 1.62 ms                                                | 1.78 ms: 1.10x slower                                                     |
| coverage                 | 79.4 ms                                                | 91.4 ms: 1.15x slower                                                     |
| python_startup_no_site   | 5.93 ms                                                | 7.20 ms: 1.21x slower                                                     |
| docutils                 | 3.30 sec                                               | 6.89 sec: 2.09x slower                                                    |
| raytrace                 | 507 ms                                                 | 5.00 sec: 9.87x slower                                                    |
| Geometric mean           | (ref)                                                  | 1.35x faster                                                              |

Benchmark hidden because not significant (1): bench_mp_pool
Ignored benchmarks (17) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, djangocms, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (5) of results/bm-20240807-3.14.0a0-c232e47-JIT/bm-20240807-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-c232e47.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.28x
- 95% likely to have a speedup of 1.25x
- 99% likely to have a speedup of 1.21x

# Memory
- memory change: 1.23x