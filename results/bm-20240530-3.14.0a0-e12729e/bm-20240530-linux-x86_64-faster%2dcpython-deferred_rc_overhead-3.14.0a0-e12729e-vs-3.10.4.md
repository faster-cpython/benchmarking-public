# Results vs. 3.10.4

- fork: faster-cpython
- ref: deferred_rc_overhead
- machine: linux-x86_64
- commit hash: e12729e
- commit date: 2024-05-30
- overall geometric mean: 1.32x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.25x faster
- Memory change: 1.11x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240530-linux-x86_64-faster%2dcpython-deferred_rc_overhead-3.14.0a0-e12729e |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 274 ms: 1.27x faster                                                            |
| docutils       | 3.30 sec                                               | 2.81 sec: 1.17x faster                                                          |
| html5lib       | 88.9 ms                                                | 66.7 ms: 1.33x faster                                                           |
| tornado_http   | 136 ms                                                 | 94.3 ms: 1.45x faster                                                           |
| Geometric mean | (ref)                                                  | 1.30x faster                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240530-linux-x86_64-faster%2dcpython-deferred_rc_overhead-3.14.0a0-e12729e |
|-------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_none         | 728 ms                                                 | 389 ms: 1.87x faster                                                            |
| async_tree_io           | 1.77 sec                                               | 951 ms: 1.86x faster                                                            |
| async_tree_memoization  | 870 ms                                                 | 480 ms: 1.81x faster                                                            |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 622 ms: 1.63x faster                                                            |
| Geometric mean          | (ref)                                                  | 1.79x faster                                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240530-linux-x86_64-faster%2dcpython-deferred_rc_overhead-3.14.0a0-e12729e |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 92.4 ms: 1.66x faster                                                           |
| float          | 117 ms                                                 | 79.6 ms: 1.47x faster                                                           |
| pidigits       | 191 ms                                                 | 189 ms: 1.01x faster                                                            |
| Geometric mean | (ref)                                                  | 1.35x faster                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240530-linux-x86_64-faster%2dcpython-deferred_rc_overhead-3.14.0a0-e12729e |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 137 ms: 1.37x faster                                                            |
| regex_v8       | 27.8 ms                                                | 24.6 ms: 1.13x faster                                                           |
| regex_dna      | 227 ms                                                 | 226 ms: 1.00x faster                                                            |
| regex_effbot   | 3.63 ms                                                | 3.80 ms: 1.05x slower                                                           |
| Geometric mean | (ref)                                                  | 1.10x faster                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240530-linux-x86_64-faster%2dcpython-deferred_rc_overhead-3.14.0a0-e12729e |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| pickle_pure_python   | 484 us                                                 | 313 us: 1.55x faster                                                            |
| unpickle_pure_python | 331 us                                                 | 225 us: 1.47x faster                                                            |
| tomli_loads          | 3.14 sec                                               | 2.22 sec: 1.41x faster                                                          |
| json_dumps           | 14.2 ms                                                | 10.6 ms: 1.34x faster                                                           |
| xml_etree_process    | 79.1 ms                                                | 61.3 ms: 1.29x faster                                                           |
| xml_etree_generate   | 99.4 ms                                                | 88.3 ms: 1.13x faster                                                           |
| json_loads           | 31.2 us                                                | 28.9 us: 1.08x faster                                                           |
| xml_etree_iterparse  | 115 ms                                                 | 108 ms: 1.07x faster                                                            |
| xml_etree_parse      | 168 ms                                                 | 160 ms: 1.05x faster                                                            |
| pickle_list          | 5.08 us                                                | 5.14 us: 1.01x slower                                                           |
| unpickle_list        | 5.20 us                                                | 5.43 us: 1.05x slower                                                           |
| unpickle             | 14.4 us                                                | 15.3 us: 1.06x slower                                                           |
| pickle               | 10.7 us                                                | 11.7 us: 1.10x slower                                                           |
| pickle_dict          | 29.6 us                                                | 35.3 us: 1.19x slower                                                           |
| Geometric mean       | (ref)                                                  | 1.12x faster                                                                    |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240530-linux-x86_64-faster%2dcpython-deferred_rc_overhead-3.14.0a0-e12729e |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 10.6 ms: 1.38x faster                                                           |
| python_startup_no_site | 5.93 ms                                                | 7.08 ms: 1.19x slower                                                           |
| Geometric mean         | (ref)                                                  | 1.08x faster                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240530-linux-x86_64-faster%2dcpython-deferred_rc_overhead-3.14.0a0-e12729e |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mako            | 16.3 ms                                                | 11.4 ms: 1.44x faster                                                           |
| django_template | 48.2 ms                                                | 35.8 ms: 1.34x faster                                                           |
| genshi_text     | 31.8 ms                                                | 24.0 ms: 1.33x faster                                                           |
| genshi_xml      | 66.0 ms                                                | 52.6 ms: 1.25x faster                                                           |
| Geometric mean  | (ref)                                                  | 1.34x faster                                                                    |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240530-linux-x86_64-faster%2dcpython-deferred_rc_overhead-3.14.0a0-e12729e |
|--------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 172 us: 3.17x faster                                                            |
| generators               | 80.1 ms                                                | 29.9 ms: 2.68x faster                                                           |
| deltablue                | 7.91 ms                                                | 3.33 ms: 2.38x faster                                                           |
| async_tree_none          | 728 ms                                                 | 389 ms: 1.87x faster                                                            |
| async_tree_io            | 1.77 sec                                               | 951 ms: 1.86x faster                                                            |
| raytrace                 | 507 ms                                                 | 274 ms: 1.85x faster                                                            |
| chaos                    | 115 ms                                                 | 62.6 ms: 1.84x faster                                                           |
| logging_silent           | 190 ns                                                 | 103 ns: 1.84x faster                                                            |
| asyncio_tcp              | 922 ms                                                 | 508 ms: 1.81x faster                                                            |
| async_tree_memoization   | 870 ms                                                 | 480 ms: 1.81x faster                                                            |
| pylint                   | 551 ms                                                 | 319 ms: 1.73x faster                                                            |
| scimark_sor              | 220 ms                                                 | 128 ms: 1.72x faster                                                            |
| comprehensions           | 28.8 us                                                | 17.0 us: 1.69x faster                                                           |
| richards_super           | 94.7 ms                                                | 56.2 ms: 1.69x faster                                                           |
| nbody                    | 154 ms                                                 | 92.4 ms: 1.66x faster                                                           |
| scimark_monte_carlo      | 118 ms                                                 | 71.9 ms: 1.65x faster                                                           |
| crypto_pyaes             | 128 ms                                                 | 78.0 ms: 1.64x faster                                                           |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 622 ms: 1.63x faster                                                            |
| go                       | 240 ms                                                 | 147 ms: 1.63x faster                                                            |
| hexiom                   | 10.4 ms                                                | 6.43 ms: 1.62x faster                                                           |
| sqlglot_parse            | 2.17 ms                                                | 1.35 ms: 1.61x faster                                                           |
| richards                 | 79.3 ms                                                | 49.8 ms: 1.59x faster                                                           |
| sqlglot_transpile        | 2.57 ms                                                | 1.65 ms: 1.56x faster                                                           |
| pickle_pure_python       | 484 us                                                 | 313 us: 1.55x faster                                                            |
| coroutines               | 35.1 ms                                                | 23.7 ms: 1.48x faster                                                           |
| float                    | 117 ms                                                 | 79.6 ms: 1.47x faster                                                           |
| unpickle_pure_python     | 331 us                                                 | 225 us: 1.47x faster                                                            |
| scimark_lu               | 176 ms                                                 | 120 ms: 1.47x faster                                                            |
| pyflate                  | 716 ms                                                 | 488 ms: 1.47x faster                                                            |
| tornado_http             | 136 ms                                                 | 94.3 ms: 1.45x faster                                                           |
| spectral_norm            | 170 ms                                                 | 118 ms: 1.44x faster                                                            |
| mako                     | 16.3 ms                                                | 11.4 ms: 1.44x faster                                                           |
| logging_simple           | 8.30 us                                                | 5.80 us: 1.43x faster                                                           |
| tomli_loads              | 3.14 sec                                               | 2.22 sec: 1.41x faster                                                          |
| deepcopy_memo            | 58.5 us                                                | 41.5 us: 1.41x faster                                                           |
| logging_format           | 9.09 us                                                | 6.47 us: 1.41x faster                                                           |
| asyncio_tcp_ssl          | 2.57 sec                                               | 1.85 sec: 1.39x faster                                                          |
| python_startup           | 14.6 ms                                                | 10.6 ms: 1.38x faster                                                           |
| regex_compile            | 188 ms                                                 | 137 ms: 1.37x faster                                                            |
| pycparser                | 1.58 sec                                               | 1.16 sec: 1.36x faster                                                          |
| django_template          | 48.2 ms                                                | 35.8 ms: 1.34x faster                                                           |
| json_dumps               | 14.2 ms                                                | 10.6 ms: 1.34x faster                                                           |
| pprint_pformat           | 2.10 sec                                               | 1.57 sec: 1.34x faster                                                          |
| html5lib                 | 88.9 ms                                                | 66.7 ms: 1.33x faster                                                           |
| genshi_text              | 31.8 ms                                                | 24.0 ms: 1.33x faster                                                           |
| thrift                   | 1.07 ms                                                | 815 us: 1.32x faster                                                            |
| pprint_safe_repr         | 1.02 sec                                               | 774 ms: 1.31x faster                                                            |
| fannkuch                 | 532 ms                                                 | 406 ms: 1.31x faster                                                            |
| xml_etree_process        | 79.1 ms                                                | 61.3 ms: 1.29x faster                                                           |
| deepcopy                 | 479 us                                                 | 374 us: 1.28x faster                                                            |
| sqlglot_normalize        | 143 ms                                                 | 112 ms: 1.28x faster                                                            |
| 2to3                     | 348 ms                                                 | 274 ms: 1.27x faster                                                            |
| nqueens                  | 106 ms                                                 | 83.2 ms: 1.27x faster                                                           |
| dulwich_log              | 84.3 ms                                                | 66.6 ms: 1.27x faster                                                           |
| pathlib                  | 20.5 ms                                                | 16.2 ms: 1.26x faster                                                           |
| genshi_xml               | 66.0 ms                                                | 52.6 ms: 1.25x faster                                                           |
| sympy_sum                | 196 ms                                                 | 157 ms: 1.25x faster                                                            |
| sympy_integrate          | 25.8 ms                                                | 20.7 ms: 1.25x faster                                                           |
| deepcopy_reduce          | 4.17 us                                                | 3.35 us: 1.24x faster                                                           |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 5.25 ms: 1.23x faster                                                           |
| sqlglot_optimize         | 69.2 ms                                                | 56.3 ms: 1.23x faster                                                           |
| sympy_str                | 346 ms                                                 | 284 ms: 1.22x faster                                                            |
| scimark_fft              | 466 ms                                                 | 384 ms: 1.21x faster                                                            |
| dask                     | 441 ms                                                 | 370 ms: 1.19x faster                                                            |
| sympy_expand             | 566 ms                                                 | 477 ms: 1.19x faster                                                            |
| bench_thread_pool        | 986 us                                                 | 836 us: 1.18x faster                                                            |
| docutils                 | 3.30 sec                                               | 2.81 sec: 1.17x faster                                                          |
| regex_v8                 | 27.8 ms                                                | 24.6 ms: 1.13x faster                                                           |
| xml_etree_generate       | 99.4 ms                                                | 88.3 ms: 1.13x faster                                                           |
| mdp                      | 2.85 sec                                               | 2.59 sec: 1.10x faster                                                          |
| json                     | 5.69 ms                                                | 5.28 ms: 1.08x faster                                                           |
| json_loads               | 31.2 us                                                | 28.9 us: 1.08x faster                                                           |
| xml_etree_iterparse      | 115 ms                                                 | 108 ms: 1.07x faster                                                            |
| meteor_contest           | 120 ms                                                 | 112 ms: 1.07x faster                                                            |
| xml_etree_parse          | 168 ms                                                 | 160 ms: 1.05x faster                                                            |
| sqlite_synth             | 3.02 us                                                | 2.98 us: 1.01x faster                                                           |
| pidigits                 | 191 ms                                                 | 189 ms: 1.01x faster                                                            |
| bench_mp_pool            | 24.0 ms                                                | 23.9 ms: 1.01x faster                                                           |
| regex_dna                | 227 ms                                                 | 226 ms: 1.00x faster                                                            |
| asyncio_websockets       | 559 ms                                                 | 566 ms: 1.01x slower                                                            |
| pickle_list              | 5.08 us                                                | 5.14 us: 1.01x slower                                                           |
| async_generators         | 444 ms                                                 | 452 ms: 1.02x slower                                                            |
| gc_traversal             | 3.62 ms                                                | 3.72 ms: 1.03x slower                                                           |
| unpickle_list            | 5.20 us                                                | 5.43 us: 1.05x slower                                                           |
| regex_effbot             | 3.63 ms                                                | 3.80 ms: 1.05x slower                                                           |
| unpickle                 | 14.4 us                                                | 15.3 us: 1.06x slower                                                           |
| pickle                   | 10.7 us                                                | 11.7 us: 1.10x slower                                                           |
| create_gc_cycles         | 1.62 ms                                                | 1.79 ms: 1.11x slower                                                           |
| coverage                 | 79.4 ms                                                | 93.6 ms: 1.18x slower                                                           |
| telco                    | 7.27 ms                                                | 8.60 ms: 1.18x slower                                                           |
| pickle_dict              | 29.6 us                                                | 35.3 us: 1.19x slower                                                           |
| python_startup_no_site   | 5.93 ms                                                | 7.08 ms: 1.19x slower                                                           |
| Geometric mean           | (ref)                                                  | 1.32x faster                                                                    |
Ignored benchmarks (9) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, djangocms, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
Ignored benchmarks (4) of results/bm-20240530-3.14.0a0-e12729e/bm-20240530-linux-x86_64-faster%2dcpython-deferred_rc_overhead-3.14.0a0-e12729e.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.27x
- 95% likely to have a speedup of 1.27x
- 99% likely to have a speedup of 1.25x

# Memory
- memory change: 1.11x