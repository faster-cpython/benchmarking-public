# Results vs. 3.10.4

- fork: brandtbucher
- ref: tier_two_constants
- machine: linux-x86_64
- commit hash: c5de9e3
- commit date: 2024-09-05
- overall geometric mean: 1.43x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.27x faster
- Memory change: 1.21x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240905-linux-x86_64-brandtbucher-tier_two_constants-3.14.0a0-c5de9e3 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 274 ms: 1.27x faster                                                      |
| docutils       | 3.30 sec                                               | 3.02 sec: 1.09x faster                                                    |
| html5lib       | 88.9 ms                                                | 64.3 ms: 1.38x faster                                                     |
| tornado_http   | 136 ms                                                 | 95.5 ms: 1.43x faster                                                     |
| Geometric mean | (ref)                                                  | 1.29x faster                                                              |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240905-linux-x86_64-brandtbucher-tier_two_constants-3.14.0a0-c5de9e3 |
|-------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| async_tree_none         | 728 ms                                                 | 327 ms: 2.22x faster                                                      |
| async_tree_memoization  | 870 ms                                                 | 401 ms: 2.17x faster                                                      |
| async_tree_io           | 1.77 sec                                               | 932 ms: 1.90x faster                                                      |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 556 ms: 1.83x faster                                                      |
| Geometric mean          | (ref)                                                  | 2.02x faster                                                              |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240905-linux-x86_64-brandtbucher-tier_two_constants-3.14.0a0-c5de9e3 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 80.7 ms: 1.90x faster                                                     |
| float          | 117 ms                                                 | 71.4 ms: 1.64x faster                                                     |
| pidigits       | 191 ms                                                 | 187 ms: 1.02x faster                                                      |
| Geometric mean | (ref)                                                  | 1.47x faster                                                              |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240905-linux-x86_64-brandtbucher-tier_two_constants-3.14.0a0-c5de9e3 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 140 ms: 1.35x faster                                                      |
| regex_v8       | 27.8 ms                                                | 24.4 ms: 1.14x faster                                                     |
| regex_dna      | 227 ms                                                 | 215 ms: 1.05x faster                                                      |
| Geometric mean | (ref)                                                  | 1.13x faster                                                              |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240905-linux-x86_64-brandtbucher-tier_two_constants-3.14.0a0-c5de9e3 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| tomli_loads          | 3.14 sec                                               | 1.92 sec: 1.64x faster                                                    |
| pickle_pure_python   | 484 us                                                 | 298 us: 1.63x faster                                                      |
| unpickle_pure_python | 331 us                                                 | 211 us: 1.56x faster                                                      |
| xml_etree_process    | 79.1 ms                                                | 54.7 ms: 1.45x faster                                                     |
| json_dumps           | 14.2 ms                                                | 10.4 ms: 1.37x faster                                                     |
| xml_etree_generate   | 99.4 ms                                                | 77.6 ms: 1.28x faster                                                     |
| xml_etree_iterparse  | 115 ms                                                 | 98.6 ms: 1.17x faster                                                     |
| xml_etree_parse      | 168 ms                                                 | 148 ms: 1.14x faster                                                      |
| json_loads           | 31.2 us                                                | 28.6 us: 1.09x faster                                                     |
| Geometric mean       | (ref)                                                  | 1.35x faster                                                              |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240905-linux-x86_64-brandtbucher-tier_two_constants-3.14.0a0-c5de9e3 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 10.6 ms: 1.38x faster                                                     |
| python_startup_no_site | 5.93 ms                                                | 7.18 ms: 1.21x slower                                                     |
| Geometric mean         | (ref)                                                  | 1.07x faster                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240905-linux-x86_64-brandtbucher-tier_two_constants-3.14.0a0-c5de9e3 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| mako            | 16.3 ms                                                | 9.86 ms: 1.66x faster                                                     |
| django_template | 48.2 ms                                                | 35.5 ms: 1.36x faster                                                     |
| genshi_text     | 31.8 ms                                                | 24.9 ms: 1.28x faster                                                     |
| genshi_xml      | 66.0 ms                                                | 59.4 ms: 1.11x faster                                                     |
| Geometric mean  | (ref)                                                  | 1.34x faster                                                              |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240905-linux-x86_64-brandtbucher-tier_two_constants-3.14.0a0-c5de9e3 |
|--------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 162 us: 3.35x faster                                                      |
| deltablue                | 7.91 ms                                                | 3.19 ms: 2.48x faster                                                     |
| generators               | 80.1 ms                                                | 33.1 ms: 2.42x faster                                                     |
| async_tree_none          | 728 ms                                                 | 327 ms: 2.22x faster                                                      |
| deepcopy_memo            | 58.5 us                                                | 26.6 us: 2.20x faster                                                     |
| async_tree_memoization   | 870 ms                                                 | 401 ms: 2.17x faster                                                      |
| richards_super           | 94.7 ms                                                | 44.9 ms: 2.11x faster                                                     |
| richards                 | 79.3 ms                                                | 39.1 ms: 2.03x faster                                                     |
| chaos                    | 115 ms                                                 | 58.3 ms: 1.98x faster                                                     |
| crypto_pyaes             | 128 ms                                                 | 66.2 ms: 1.93x faster                                                     |
| logging_silent           | 190 ns                                                 | 99.5 ns: 1.91x faster                                                     |
| nbody                    | 154 ms                                                 | 80.7 ms: 1.90x faster                                                     |
| async_tree_io            | 1.77 sec                                               | 932 ms: 1.90x faster                                                      |
| scimark_sor              | 220 ms                                                 | 116 ms: 1.89x faster                                                      |
| scimark_monte_carlo      | 118 ms                                                 | 62.5 ms: 1.89x faster                                                     |
| asyncio_tcp              | 922 ms                                                 | 488 ms: 1.89x faster                                                      |
| go                       | 240 ms                                                 | 130 ms: 1.85x faster                                                      |
| raytrace                 | 507 ms                                                 | 276 ms: 1.83x faster                                                      |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 556 ms: 1.83x faster                                                      |
| deepcopy                 | 479 us                                                 | 266 us: 1.80x faster                                                      |
| comprehensions           | 28.8 us                                                | 16.7 us: 1.72x faster                                                     |
| spectral_norm            | 170 ms                                                 | 99.1 ms: 1.71x faster                                                     |
| mako                     | 16.3 ms                                                | 9.86 ms: 1.66x faster                                                     |
| float                    | 117 ms                                                 | 71.4 ms: 1.64x faster                                                     |
| tomli_loads              | 3.14 sec                                               | 1.92 sec: 1.64x faster                                                    |
| sqlglot_parse            | 2.17 ms                                                | 1.33 ms: 1.63x faster                                                     |
| pickle_pure_python       | 484 us                                                 | 298 us: 1.63x faster                                                      |
| pyflate                  | 716 ms                                                 | 451 ms: 1.59x faster                                                      |
| deepcopy_reduce          | 4.17 us                                                | 2.65 us: 1.57x faster                                                     |
| unpickle_pure_python     | 331 us                                                 | 211 us: 1.56x faster                                                      |
| scimark_lu               | 176 ms                                                 | 113 ms: 1.56x faster                                                      |
| coroutines               | 35.1 ms                                                | 22.7 ms: 1.55x faster                                                     |
| sqlglot_transpile        | 2.57 ms                                                | 1.68 ms: 1.53x faster                                                     |
| scimark_fft              | 466 ms                                                 | 307 ms: 1.52x faster                                                      |
| hexiom                   | 10.4 ms                                                | 6.85 ms: 1.52x faster                                                     |
| pylint                   | 551 ms                                                 | 372 ms: 1.48x faster                                                      |
| logging_simple           | 8.30 us                                                | 5.65 us: 1.47x faster                                                     |
| logging_format           | 9.09 us                                                | 6.24 us: 1.46x faster                                                     |
| xml_etree_process        | 79.1 ms                                                | 54.7 ms: 1.45x faster                                                     |
| asyncio_tcp_ssl          | 2.57 sec                                               | 1.80 sec: 1.43x faster                                                    |
| fannkuch                 | 532 ms                                                 | 372 ms: 1.43x faster                                                      |
| tornado_http             | 136 ms                                                 | 95.5 ms: 1.43x faster                                                     |
| pprint_safe_repr         | 1.02 sec                                               | 713 ms: 1.43x faster                                                      |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.55 ms: 1.42x faster                                                     |
| pprint_pformat           | 2.10 sec                                               | 1.49 sec: 1.41x faster                                                    |
| thrift                   | 1.07 ms                                                | 776 us: 1.38x faster                                                      |
| html5lib                 | 88.9 ms                                                | 64.3 ms: 1.38x faster                                                     |
| python_startup           | 14.6 ms                                                | 10.6 ms: 1.38x faster                                                     |
| json_dumps               | 14.2 ms                                                | 10.4 ms: 1.37x faster                                                     |
| django_template          | 48.2 ms                                                | 35.5 ms: 1.36x faster                                                     |
| regex_compile            | 188 ms                                                 | 140 ms: 1.35x faster                                                      |
| pycparser                | 1.58 sec                                               | 1.18 sec: 1.34x faster                                                    |
| pathlib                  | 20.5 ms                                                | 16.0 ms: 1.28x faster                                                     |
| xml_etree_generate       | 99.4 ms                                                | 77.6 ms: 1.28x faster                                                     |
| genshi_text              | 31.8 ms                                                | 24.9 ms: 1.28x faster                                                     |
| sqlglot_normalize        | 143 ms                                                 | 112 ms: 1.27x faster                                                      |
| 2to3                     | 348 ms                                                 | 274 ms: 1.27x faster                                                      |
| nqueens                  | 106 ms                                                 | 85.2 ms: 1.24x faster                                                     |
| dulwich_log              | 84.3 ms                                                | 68.1 ms: 1.24x faster                                                     |
| sqlglot_optimize         | 69.2 ms                                                | 58.3 ms: 1.19x faster                                                     |
| bench_thread_pool        | 986 us                                                 | 833 us: 1.18x faster                                                      |
| xml_etree_iterparse      | 115 ms                                                 | 98.6 ms: 1.17x faster                                                     |
| sympy_str                | 346 ms                                                 | 300 ms: 1.15x faster                                                      |
| xml_etree_parse          | 168 ms                                                 | 148 ms: 1.14x faster                                                      |
| regex_v8                 | 27.8 ms                                                | 24.4 ms: 1.14x faster                                                     |
| sympy_sum                | 196 ms                                                 | 173 ms: 1.14x faster                                                      |
| sympy_integrate          | 25.8 ms                                                | 22.8 ms: 1.13x faster                                                     |
| mdp                      | 2.85 sec                                               | 2.53 sec: 1.13x faster                                                    |
| meteor_contest           | 120 ms                                                 | 107 ms: 1.12x faster                                                      |
| sympy_expand             | 566 ms                                                 | 507 ms: 1.12x faster                                                      |
| genshi_xml               | 66.0 ms                                                | 59.4 ms: 1.11x faster                                                     |
| docutils                 | 3.30 sec                                               | 3.02 sec: 1.09x faster                                                    |
| json_loads               | 31.2 us                                                | 28.6 us: 1.09x faster                                                     |
| json                     | 5.69 ms                                                | 5.32 ms: 1.07x faster                                                     |
| regex_dna                | 227 ms                                                 | 215 ms: 1.05x faster                                                      |
| pidigits                 | 191 ms                                                 | 187 ms: 1.02x faster                                                      |
| asyncio_websockets       | 559 ms                                                 | 555 ms: 1.01x faster                                                      |
| gc_traversal             | 3.62 ms                                                | 3.62 ms: 1.00x faster                                                     |
| async_generators         | 444 ms                                                 | 453 ms: 1.02x slower                                                      |
| telco                    | 7.27 ms                                                | 7.89 ms: 1.09x slower                                                     |
| create_gc_cycles         | 1.62 ms                                                | 1.78 ms: 1.10x slower                                                     |
| coverage                 | 79.4 ms                                                | 94.0 ms: 1.18x slower                                                     |
| python_startup_no_site   | 5.93 ms                                                | 7.18 ms: 1.21x slower                                                     |
| Geometric mean           | (ref)                                                  | 1.43x faster                                                              |

Benchmark hidden because not significant (2): bench_mp_pool, regex_effbot
Ignored benchmarks (16) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (5) of results/bm-20240905-3.14.0a0-c5de9e3-JIT/bm-20240905-linux-x86_64-brandtbucher-tier_two_constants-3.14.0a0-c5de9e3.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.31x
- 95% likely to have a speedup of 1.30x
- 99% likely to have a speedup of 1.27x

# Memory
- memory change: 1.21x