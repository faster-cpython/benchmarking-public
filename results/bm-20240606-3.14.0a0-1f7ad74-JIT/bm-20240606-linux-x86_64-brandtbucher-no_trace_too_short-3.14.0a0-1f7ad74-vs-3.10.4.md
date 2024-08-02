# Results vs. 3.10.4

- fork: brandtbucher
- ref: no_trace_too_short
- machine: linux-x86_64
- commit hash: 1f7ad74
- commit date: 2024-06-06
- overall geometric mean: 1.34x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.23x faster
- Memory change: 1.21x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240606-linux-x86_64-brandtbucher-no_trace_too_short-3.14.0a0-1f7ad74 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 280 ms: 1.25x faster                                                      |
| docutils       | 3.30 sec                                               | 2.97 sec: 1.11x faster                                                    |
| html5lib       | 88.9 ms                                                | 69.5 ms: 1.28x faster                                                     |
| tornado_http   | 136 ms                                                 | 96.8 ms: 1.41x faster                                                     |
| Geometric mean | (ref)                                                  | 1.26x faster                                                              |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240606-linux-x86_64-brandtbucher-no_trace_too_short-3.14.0a0-1f7ad74 |
|-------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| async_tree_none         | 728 ms                                                 | 376 ms: 1.94x faster                                                      |
| async_tree_io           | 1.77 sec                                               | 963 ms: 1.84x faster                                                      |
| async_tree_memoization  | 870 ms                                                 | 479 ms: 1.82x faster                                                      |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 633 ms: 1.61x faster                                                      |
| Geometric mean          | (ref)                                                  | 1.79x faster                                                              |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240606-linux-x86_64-brandtbucher-no_trace_too_short-3.14.0a0-1f7ad74 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 81.8 ms: 1.88x faster                                                     |
| float          | 117 ms                                                 | 73.0 ms: 1.60x faster                                                     |
| pidigits       | 191 ms                                                 | 189 ms: 1.01x faster                                                      |
| Geometric mean | (ref)                                                  | 1.45x faster                                                              |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240606-linux-x86_64-brandtbucher-no_trace_too_short-3.14.0a0-1f7ad74 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 138 ms: 1.36x faster                                                      |
| regex_v8       | 27.8 ms                                                | 26.6 ms: 1.05x faster                                                     |
| regex_dna      | 227 ms                                                 | 238 ms: 1.05x slower                                                      |
| regex_effbot   | 3.63 ms                                                | 4.01 ms: 1.10x slower                                                     |
| Geometric mean | (ref)                                                  | 1.05x faster                                                              |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240606-linux-x86_64-brandtbucher-no_trace_too_short-3.14.0a0-1f7ad74 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| tomli_loads          | 3.14 sec                                               | 1.95 sec: 1.61x faster                                                    |
| pickle_pure_python   | 484 us                                                 | 305 us: 1.59x faster                                                      |
| unpickle_pure_python | 331 us                                                 | 223 us: 1.48x faster                                                      |
| json_dumps           | 14.2 ms                                                | 10.3 ms: 1.38x faster                                                     |
| xml_etree_process    | 79.1 ms                                                | 58.3 ms: 1.36x faster                                                     |
| xml_etree_generate   | 99.4 ms                                                | 81.3 ms: 1.22x faster                                                     |
| xml_etree_iterparse  | 115 ms                                                 | 101 ms: 1.14x faster                                                      |
| xml_etree_parse      | 168 ms                                                 | 149 ms: 1.13x faster                                                      |
| json_loads           | 31.2 us                                                | 28.8 us: 1.08x faster                                                     |
| pickle_list          | 5.08 us                                                | 5.05 us: 1.01x faster                                                     |
| unpickle             | 14.4 us                                                | 14.9 us: 1.03x slower                                                     |
| unpickle_list        | 5.20 us                                                | 5.43 us: 1.04x slower                                                     |
| pickle               | 10.7 us                                                | 12.0 us: 1.12x slower                                                     |
| pickle_dict          | 29.6 us                                                | 35.2 us: 1.19x slower                                                     |
| Geometric mean       | (ref)                                                  | 1.16x faster                                                              |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240606-linux-x86_64-brandtbucher-no_trace_too_short-3.14.0a0-1f7ad74 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 11.2 ms: 1.30x faster                                                     |
| python_startup_no_site | 5.93 ms                                                | 7.62 ms: 1.28x slower                                                     |
| Geometric mean         | (ref)                                                  | 1.01x faster                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240606-linux-x86_64-brandtbucher-no_trace_too_short-3.14.0a0-1f7ad74 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| mako            | 16.3 ms                                                | 10.0 ms: 1.63x faster                                                     |
| django_template | 48.2 ms                                                | 36.8 ms: 1.31x faster                                                     |
| genshi_text     | 31.8 ms                                                | 25.0 ms: 1.27x faster                                                     |
| genshi_xml      | 66.0 ms                                                | 58.1 ms: 1.14x faster                                                     |
| Geometric mean  | (ref)                                                  | 1.33x faster                                                              |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240606-linux-x86_64-brandtbucher-no_trace_too_short-3.14.0a0-1f7ad74 |
|--------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 170 us: 3.19x faster                                                      |
| generators               | 80.1 ms                                                | 30.5 ms: 2.62x faster                                                     |
| deltablue                | 7.91 ms                                                | 3.82 ms: 2.07x faster                                                     |
| chaos                    | 115 ms                                                 | 59.4 ms: 1.94x faster                                                     |
| async_tree_none          | 728 ms                                                 | 376 ms: 1.94x faster                                                      |
| richards_super           | 94.7 ms                                                | 49.2 ms: 1.93x faster                                                     |
| scimark_monte_carlo      | 118 ms                                                 | 62.6 ms: 1.89x faster                                                     |
| crypto_pyaes             | 128 ms                                                 | 67.9 ms: 1.88x faster                                                     |
| nbody                    | 154 ms                                                 | 81.8 ms: 1.88x faster                                                     |
| richards                 | 79.3 ms                                                | 42.5 ms: 1.86x faster                                                     |
| async_tree_io            | 1.77 sec                                               | 963 ms: 1.84x faster                                                      |
| async_tree_memoization   | 870 ms                                                 | 479 ms: 1.82x faster                                                      |
| raytrace                 | 507 ms                                                 | 279 ms: 1.82x faster                                                      |
| asyncio_tcp              | 922 ms                                                 | 517 ms: 1.78x faster                                                      |
| logging_silent           | 190 ns                                                 | 108 ns: 1.75x faster                                                      |
| comprehensions           | 28.8 us                                                | 16.8 us: 1.71x faster                                                     |
| spectral_norm            | 170 ms                                                 | 102 ms: 1.66x faster                                                      |
| sqlglot_parse            | 2.17 ms                                                | 1.32 ms: 1.64x faster                                                     |
| mako                     | 16.3 ms                                                | 10.0 ms: 1.63x faster                                                     |
| go                       | 240 ms                                                 | 148 ms: 1.62x faster                                                      |
| tomli_loads              | 3.14 sec                                               | 1.95 sec: 1.61x faster                                                    |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 633 ms: 1.61x faster                                                      |
| pyflate                  | 716 ms                                                 | 446 ms: 1.60x faster                                                      |
| float                    | 117 ms                                                 | 73.0 ms: 1.60x faster                                                     |
| scimark_sor              | 220 ms                                                 | 138 ms: 1.59x faster                                                      |
| pickle_pure_python       | 484 us                                                 | 305 us: 1.59x faster                                                      |
| hexiom                   | 10.4 ms                                                | 6.59 ms: 1.58x faster                                                     |
| pylint                   | 551 ms                                                 | 354 ms: 1.56x faster                                                      |
| sqlglot_transpile        | 2.57 ms                                                | 1.66 ms: 1.55x faster                                                     |
| deepcopy_memo            | 58.5 us                                                | 38.1 us: 1.53x faster                                                     |
| coroutines               | 35.1 ms                                                | 23.0 ms: 1.53x faster                                                     |
| fannkuch                 | 532 ms                                                 | 350 ms: 1.52x faster                                                      |
| unpickle_pure_python     | 331 us                                                 | 223 us: 1.48x faster                                                      |
| logging_simple           | 8.30 us                                                | 5.66 us: 1.47x faster                                                     |
| scimark_fft              | 466 ms                                                 | 318 ms: 1.46x faster                                                      |
| logging_format           | 9.09 us                                                | 6.31 us: 1.44x faster                                                     |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.55 ms: 1.42x faster                                                     |
| pprint_pformat           | 2.10 sec                                               | 1.49 sec: 1.41x faster                                                    |
| tornado_http             | 136 ms                                                 | 96.8 ms: 1.41x faster                                                     |
| pprint_safe_repr         | 1.02 sec                                               | 724 ms: 1.41x faster                                                      |
| scimark_lu               | 176 ms                                                 | 126 ms: 1.40x faster                                                      |
| asyncio_tcp_ssl          | 2.57 sec                                               | 1.85 sec: 1.39x faster                                                    |
| json_dumps               | 14.2 ms                                                | 10.3 ms: 1.38x faster                                                     |
| regex_compile            | 188 ms                                                 | 138 ms: 1.36x faster                                                      |
| xml_etree_process        | 79.1 ms                                                | 58.3 ms: 1.36x faster                                                     |
| thrift                   | 1.07 ms                                                | 818 us: 1.31x faster                                                      |
| django_template          | 48.2 ms                                                | 36.8 ms: 1.31x faster                                                     |
| python_startup           | 14.6 ms                                                | 11.2 ms: 1.30x faster                                                     |
| pycparser                | 1.58 sec                                               | 1.22 sec: 1.29x faster                                                    |
| deepcopy                 | 479 us                                                 | 373 us: 1.28x faster                                                      |
| html5lib                 | 88.9 ms                                                | 69.5 ms: 1.28x faster                                                     |
| genshi_text              | 31.8 ms                                                | 25.0 ms: 1.27x faster                                                     |
| sqlglot_normalize        | 143 ms                                                 | 114 ms: 1.26x faster                                                      |
| 2to3                     | 348 ms                                                 | 280 ms: 1.25x faster                                                      |
| deepcopy_reduce          | 4.17 us                                                | 3.36 us: 1.24x faster                                                     |
| pathlib                  | 20.5 ms                                                | 16.6 ms: 1.23x faster                                                     |
| dulwich_log              | 84.3 ms                                                | 68.3 ms: 1.23x faster                                                     |
| nqueens                  | 106 ms                                                 | 85.7 ms: 1.23x faster                                                     |
| xml_etree_generate       | 99.4 ms                                                | 81.3 ms: 1.22x faster                                                     |
| sqlglot_optimize         | 69.2 ms                                                | 57.0 ms: 1.21x faster                                                     |
| dask                     | 441 ms                                                 | 379 ms: 1.16x faster                                                      |
| sympy_sum                | 196 ms                                                 | 172 ms: 1.14x faster                                                      |
| xml_etree_iterparse      | 115 ms                                                 | 101 ms: 1.14x faster                                                      |
| sympy_str                | 346 ms                                                 | 303 ms: 1.14x faster                                                      |
| genshi_xml               | 66.0 ms                                                | 58.1 ms: 1.14x faster                                                     |
| sympy_integrate          | 25.8 ms                                                | 22.7 ms: 1.14x faster                                                     |
| xml_etree_parse          | 168 ms                                                 | 149 ms: 1.13x faster                                                      |
| bench_thread_pool        | 986 us                                                 | 882 us: 1.12x faster                                                      |
| docutils                 | 3.30 sec                                               | 2.97 sec: 1.11x faster                                                    |
| mdp                      | 2.85 sec                                               | 2.58 sec: 1.11x faster                                                    |
| meteor_contest           | 120 ms                                                 | 109 ms: 1.10x faster                                                      |
| sympy_expand             | 566 ms                                                 | 515 ms: 1.10x faster                                                      |
| json_loads               | 31.2 us                                                | 28.8 us: 1.08x faster                                                     |
| sqlite_synth             | 3.02 us                                                | 2.84 us: 1.07x faster                                                     |
| json                     | 5.69 ms                                                | 5.38 ms: 1.06x faster                                                     |
| regex_v8                 | 27.8 ms                                                | 26.6 ms: 1.05x faster                                                     |
| pidigits                 | 191 ms                                                 | 189 ms: 1.01x faster                                                      |
| pickle_list              | 5.08 us                                                | 5.05 us: 1.01x faster                                                     |
| asyncio_websockets       | 559 ms                                                 | 568 ms: 1.02x slower                                                      |
| unpickle                 | 14.4 us                                                | 14.9 us: 1.03x slower                                                     |
| async_generators         | 444 ms                                                 | 462 ms: 1.04x slower                                                      |
| unpickle_list            | 5.20 us                                                | 5.43 us: 1.04x slower                                                     |
| regex_dna                | 227 ms                                                 | 238 ms: 1.05x slower                                                      |
| gc_traversal             | 3.62 ms                                                | 3.83 ms: 1.06x slower                                                     |
| regex_effbot             | 3.63 ms                                                | 4.01 ms: 1.10x slower                                                     |
| telco                    | 7.27 ms                                                | 8.06 ms: 1.11x slower                                                     |
| create_gc_cycles         | 1.62 ms                                                | 1.81 ms: 1.12x slower                                                     |
| pickle                   | 10.7 us                                                | 12.0 us: 1.12x slower                                                     |
| coverage                 | 79.4 ms                                                | 93.8 ms: 1.18x slower                                                     |
| pickle_dict              | 29.6 us                                                | 35.2 us: 1.19x slower                                                     |
| python_startup_no_site   | 5.93 ms                                                | 7.62 ms: 1.28x slower                                                     |
| Geometric mean           | (ref)                                                  | 1.34x faster                                                              |

Benchmark hidden because not significant (1): bench_mp_pool
Ignored benchmarks (9) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, djangocms, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
Ignored benchmarks (4) of results/bm-20240606-3.14.0a0-1f7ad74-JIT/bm-20240606-linux-x86_64-brandtbucher-no_trace_too_short-3.14.0a0-1f7ad74.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.27x
- 95% likely to have a speedup of 1.26x
- 99% likely to have a speedup of 1.23x

# Memory
- memory change: 1.21x