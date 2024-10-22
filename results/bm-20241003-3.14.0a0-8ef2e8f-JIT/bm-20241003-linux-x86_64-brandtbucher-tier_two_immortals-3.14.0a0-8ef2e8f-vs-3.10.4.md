# Results vs. 3.10.4

- fork: brandtbucher
- ref: tier_two_immortals
- machine: linux-x86_64
- commit hash: 8ef2e8f
- commit date: 2024-10-03
- overall geometric mean: 1.36x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.26x faster
- Memory change: 1.18x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241003-linux-x86_64-brandtbucher-tier_two_immortals-3.14.0a0-8ef2e8f |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 279 ms: 1.25x faster                                                      |
| docutils       | 3.30 sec                                               | 2.92 sec: 1.13x faster                                                    |
| html5lib       | 88.9 ms                                                | 64.7 ms: 1.37x faster                                                     |
| tornado_http   | 136 ms                                                 | 94.9 ms: 1.44x faster                                                     |
| Geometric mean | (ref)                                                  | 1.29x faster                                                              |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241003-linux-x86_64-brandtbucher-tier_two_immortals-3.14.0a0-8ef2e8f |
|-------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| async_tree_none         | 728 ms                                                 | 317 ms: 2.30x faster                                                      |
| async_tree_memoization  | 870 ms                                                 | 408 ms: 2.13x faster                                                      |
| async_tree_io           | 1.77 sec                                               | 885 ms: 2.00x faster                                                      |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 569 ms: 1.79x faster                                                      |
| Geometric mean          | (ref)                                                  | 2.05x faster                                                              |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241003-linux-x86_64-brandtbucher-tier_two_immortals-3.14.0a0-8ef2e8f |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 82.3 ms: 1.87x faster                                                     |
| float          | 117 ms                                                 | 71.8 ms: 1.63x faster                                                     |
| pidigits       | 191 ms                                                 | 185 ms: 1.03x faster                                                      |
| Geometric mean | (ref)                                                  | 1.46x faster                                                              |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241003-linux-x86_64-brandtbucher-tier_two_immortals-3.14.0a0-8ef2e8f |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 143 ms: 1.32x faster                                                      |
| regex_v8       | 27.8 ms                                                | 25.5 ms: 1.09x faster                                                     |
| regex_dna      | 227 ms                                                 | 221 ms: 1.03x faster                                                      |
| regex_effbot   | 3.63 ms                                                | 3.69 ms: 1.02x slower                                                     |
| Geometric mean | (ref)                                                  | 1.10x faster                                                              |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241003-linux-x86_64-brandtbucher-tier_two_immortals-3.14.0a0-8ef2e8f |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| tomli_loads          | 3.14 sec                                               | 1.90 sec: 1.65x faster                                                    |
| pickle_pure_python   | 484 us                                                 | 309 us: 1.57x faster                                                      |
| unpickle_pure_python | 331 us                                                 | 213 us: 1.55x faster                                                      |
| xml_etree_process    | 79.1 ms                                                | 54.4 ms: 1.45x faster                                                     |
| json_dumps           | 14.2 ms                                                | 10.2 ms: 1.40x faster                                                     |
| xml_etree_generate   | 99.4 ms                                                | 76.8 ms: 1.29x faster                                                     |
| xml_etree_iterparse  | 115 ms                                                 | 98.1 ms: 1.18x faster                                                     |
| xml_etree_parse      | 168 ms                                                 | 145 ms: 1.16x faster                                                      |
| json_loads           | 31.2 us                                                | 26.9 us: 1.16x faster                                                     |
| pickle_list          | 5.08 us                                                | 4.91 us: 1.03x faster                                                     |
| unpickle             | 14.4 us                                                | 15.0 us: 1.05x slower                                                     |
| pickle               | 10.7 us                                                | 11.4 us: 1.07x slower                                                     |
| pickle_dict          | 29.6 us                                                | 34.4 us: 1.16x slower                                                     |
| Geometric mean       | (ref)                                                  | 1.20x faster                                                              |

Benchmark hidden because not significant (1): unpickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241003-linux-x86_64-brandtbucher-tier_two_immortals-3.14.0a0-8ef2e8f |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 10.5 ms: 1.39x faster                                                     |
| python_startup_no_site | 5.93 ms                                                | 7.03 ms: 1.18x slower                                                     |
| Geometric mean         | (ref)                                                  | 1.08x faster                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241003-linux-x86_64-brandtbucher-tier_two_immortals-3.14.0a0-8ef2e8f |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| mako            | 16.3 ms                                                | 9.90 ms: 1.65x faster                                                     |
| django_template | 48.2 ms                                                | 36.9 ms: 1.31x faster                                                     |
| genshi_text     | 31.8 ms                                                | 25.5 ms: 1.25x faster                                                     |
| genshi_xml      | 66.0 ms                                                | 57.9 ms: 1.14x faster                                                     |
| Geometric mean  | (ref)                                                  | 1.32x faster                                                              |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241003-linux-x86_64-brandtbucher-tier_two_immortals-3.14.0a0-8ef2e8f |
|--------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 166 us: 3.28x faster                                                      |
| deltablue                | 7.91 ms                                                | 3.19 ms: 2.48x faster                                                     |
| generators               | 80.1 ms                                                | 34.5 ms: 2.32x faster                                                     |
| async_tree_none          | 728 ms                                                 | 317 ms: 2.30x faster                                                      |
| deepcopy_memo            | 58.5 us                                                | 27.1 us: 2.16x faster                                                     |
| async_tree_memoization   | 870 ms                                                 | 408 ms: 2.13x faster                                                      |
| richards_super           | 94.7 ms                                                | 44.7 ms: 2.12x faster                                                     |
| richards                 | 79.3 ms                                                | 39.5 ms: 2.01x faster                                                     |
| async_tree_io            | 1.77 sec                                               | 885 ms: 2.00x faster                                                      |
| crypto_pyaes             | 128 ms                                                 | 65.4 ms: 1.95x faster                                                     |
| chaos                    | 115 ms                                                 | 59.7 ms: 1.93x faster                                                     |
| asyncio_tcp              | 922 ms                                                 | 484 ms: 1.90x faster                                                      |
| scimark_monte_carlo      | 118 ms                                                 | 62.5 ms: 1.89x faster                                                     |
| scimark_sor              | 220 ms                                                 | 118 ms: 1.87x faster                                                      |
| nbody                    | 154 ms                                                 | 82.3 ms: 1.87x faster                                                     |
| logging_silent           | 190 ns                                                 | 104 ns: 1.82x faster                                                      |
| raytrace                 | 507 ms                                                 | 278 ms: 1.82x faster                                                      |
| go                       | 240 ms                                                 | 132 ms: 1.82x faster                                                      |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 569 ms: 1.79x faster                                                      |
| deepcopy                 | 479 us                                                 | 271 us: 1.77x faster                                                      |
| comprehensions           | 28.8 us                                                | 16.8 us: 1.72x faster                                                     |
| spectral_norm            | 170 ms                                                 | 100 ms: 1.69x faster                                                      |
| tomli_loads              | 3.14 sec                                               | 1.90 sec: 1.65x faster                                                    |
| mako                     | 16.3 ms                                                | 9.90 ms: 1.65x faster                                                     |
| pyflate                  | 716 ms                                                 | 435 ms: 1.65x faster                                                      |
| float                    | 117 ms                                                 | 71.8 ms: 1.63x faster                                                     |
| sqlglot_parse            | 2.17 ms                                                | 1.35 ms: 1.61x faster                                                     |
| scimark_lu               | 176 ms                                                 | 110 ms: 1.59x faster                                                      |
| deepcopy_reduce          | 4.17 us                                                | 2.65 us: 1.57x faster                                                     |
| pickle_pure_python       | 484 us                                                 | 309 us: 1.57x faster                                                      |
| coroutines               | 35.1 ms                                                | 22.4 ms: 1.56x faster                                                     |
| unpickle_pure_python     | 331 us                                                 | 213 us: 1.55x faster                                                      |
| sqlglot_transpile        | 2.57 ms                                                | 1.68 ms: 1.53x faster                                                     |
| scimark_fft              | 466 ms                                                 | 307 ms: 1.52x faster                                                      |
| hexiom                   | 10.4 ms                                                | 6.95 ms: 1.50x faster                                                     |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.36 ms: 1.48x faster                                                     |
| pylint                   | 551 ms                                                 | 374 ms: 1.47x faster                                                      |
| logging_simple           | 8.30 us                                                | 5.67 us: 1.46x faster                                                     |
| xml_etree_process        | 79.1 ms                                                | 54.4 ms: 1.45x faster                                                     |
| logging_format           | 9.09 us                                                | 6.28 us: 1.45x faster                                                     |
| tornado_http             | 136 ms                                                 | 94.9 ms: 1.44x faster                                                     |
| asyncio_tcp_ssl          | 2.57 sec                                               | 1.79 sec: 1.43x faster                                                    |
| fannkuch                 | 532 ms                                                 | 372 ms: 1.43x faster                                                      |
| json_dumps               | 14.2 ms                                                | 10.2 ms: 1.40x faster                                                     |
| python_startup           | 14.6 ms                                                | 10.5 ms: 1.39x faster                                                     |
| pprint_safe_repr         | 1.02 sec                                               | 740 ms: 1.38x faster                                                      |
| html5lib                 | 88.9 ms                                                | 64.7 ms: 1.37x faster                                                     |
| pprint_pformat           | 2.10 sec                                               | 1.55 sec: 1.36x faster                                                    |
| thrift                   | 1.07 ms                                                | 797 us: 1.34x faster                                                      |
| regex_compile            | 188 ms                                                 | 143 ms: 1.32x faster                                                      |
| pathlib                  | 20.5 ms                                                | 15.6 ms: 1.31x faster                                                     |
| pycparser                | 1.58 sec                                               | 1.20 sec: 1.31x faster                                                    |
| django_template          | 48.2 ms                                                | 36.9 ms: 1.31x faster                                                     |
| xml_etree_generate       | 99.4 ms                                                | 76.8 ms: 1.29x faster                                                     |
| sqlglot_normalize        | 143 ms                                                 | 114 ms: 1.25x faster                                                      |
| 2to3                     | 348 ms                                                 | 279 ms: 1.25x faster                                                      |
| genshi_text              | 31.8 ms                                                | 25.5 ms: 1.25x faster                                                     |
| dulwich_log              | 84.3 ms                                                | 68.2 ms: 1.24x faster                                                     |
| nqueens                  | 106 ms                                                 | 85.9 ms: 1.23x faster                                                     |
| xml_etree_iterparse      | 115 ms                                                 | 98.1 ms: 1.18x faster                                                     |
| xml_etree_parse          | 168 ms                                                 | 145 ms: 1.16x faster                                                      |
| json_loads               | 31.2 us                                                | 26.9 us: 1.16x faster                                                     |
| sqlglot_optimize         | 69.2 ms                                                | 60.3 ms: 1.15x faster                                                     |
| genshi_xml               | 66.0 ms                                                | 57.9 ms: 1.14x faster                                                     |
| sympy_str                | 346 ms                                                 | 303 ms: 1.14x faster                                                      |
| docutils                 | 3.30 sec                                               | 2.92 sec: 1.13x faster                                                    |
| json                     | 5.69 ms                                                | 5.06 ms: 1.13x faster                                                     |
| sympy_sum                | 196 ms                                                 | 175 ms: 1.12x faster                                                      |
| mdp                      | 2.85 sec                                               | 2.54 sec: 1.12x faster                                                    |
| sympy_expand             | 566 ms                                                 | 505 ms: 1.12x faster                                                      |
| meteor_contest           | 120 ms                                                 | 107 ms: 1.12x faster                                                      |
| bench_thread_pool        | 986 us                                                 | 896 us: 1.10x faster                                                      |
| sympy_integrate          | 25.8 ms                                                | 23.4 ms: 1.10x faster                                                     |
| sqlite_synth             | 3.02 us                                                | 2.76 us: 1.10x faster                                                     |
| regex_v8                 | 27.8 ms                                                | 25.5 ms: 1.09x faster                                                     |
| pickle_list              | 5.08 us                                                | 4.91 us: 1.03x faster                                                     |
| pidigits                 | 191 ms                                                 | 185 ms: 1.03x faster                                                      |
| regex_dna                | 227 ms                                                 | 221 ms: 1.03x faster                                                      |
| regex_effbot             | 3.63 ms                                                | 3.69 ms: 1.02x slower                                                     |
| async_generators         | 444 ms                                                 | 452 ms: 1.02x slower                                                      |
| telco                    | 7.27 ms                                                | 7.49 ms: 1.03x slower                                                     |
| unpickle                 | 14.4 us                                                | 15.0 us: 1.05x slower                                                     |
| gc_traversal             | 3.62 ms                                                | 3.85 ms: 1.06x slower                                                     |
| pickle                   | 10.7 us                                                | 11.4 us: 1.07x slower                                                     |
| create_gc_cycles         | 1.62 ms                                                | 1.73 ms: 1.07x slower                                                     |
| coverage                 | 79.4 ms                                                | 85.8 ms: 1.08x slower                                                     |
| pickle_dict              | 29.6 us                                                | 34.4 us: 1.16x slower                                                     |
| python_startup_no_site   | 5.93 ms                                                | 7.03 ms: 1.18x slower                                                     |
| unpack_sequence          | 60.0 ns                                                | 108 ns: 1.81x slower                                                      |
| bench_mp_pool            | 24.0 ms                                                | 60.2 ms: 2.51x slower                                                     |
| Geometric mean           | (ref)                                                  | 1.36x faster                                                              |

Benchmark hidden because not significant (2): unpickle_list, asyncio_websockets
Ignored benchmarks (9) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (5) of results/bm-20241003-3.14.0a0-8ef2e8f-JIT/bm-20241003-linux-x86_64-brandtbucher-tier_two_immortals-3.14.0a0-8ef2e8f.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.32x
- 95% likely to have a speedup of 1.29x
- 99% likely to have a speedup of 1.26x

# Memory
- memory change: 1.18x