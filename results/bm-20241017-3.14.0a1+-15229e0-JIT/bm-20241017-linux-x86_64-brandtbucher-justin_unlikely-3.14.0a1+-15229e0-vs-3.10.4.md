# Results vs. 3.10.4

- fork: brandtbucher
- ref: justin_unlikely
- machine: linux-x86_64
- commit hash: 15229e0
- commit date: 2024-10-17
- overall geometric mean: 1.397x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.25x faster
- Memory change: 1.33x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241017-linux-x86_64-brandtbucher-justin_unlikely-3.14.0a1+-15229e0 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 278 ms: 1.26x faster                                                    |
| docutils       | 3.30 sec                                               | 2.92 sec: 1.13x faster                                                  |
| html5lib       | 88.9 ms                                                | 63.4 ms: 1.40x faster                                                   |
| tornado_http   | 136 ms                                                 | 95.4 ms: 1.43x faster                                                   |
| Geometric mean | (ref)                                                  | 1.30x faster                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241017-linux-x86_64-brandtbucher-justin_unlikely-3.14.0a1+-15229e0 |
|-------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_none         | 728 ms                                                 | 328 ms: 2.22x faster                                                    |
| async_tree_memoization  | 870 ms                                                 | 414 ms: 2.10x faster                                                    |
| async_tree_io           | 1.77 sec                                               | 859 ms: 2.06x faster                                                    |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 574 ms: 1.77x faster                                                    |
| Geometric mean          | (ref)                                                  | 2.03x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241017-linux-x86_64-brandtbucher-justin_unlikely-3.14.0a1+-15229e0 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 80.9 ms: 1.90x faster                                                   |
| float          | 117 ms                                                 | 75.3 ms: 1.56x faster                                                   |
| pidigits       | 191 ms                                                 | 187 ms: 1.02x faster                                                    |
| Geometric mean | (ref)                                                  | 1.44x faster                                                            |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241017-linux-x86_64-brandtbucher-justin_unlikely-3.14.0a1+-15229e0 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 141 ms: 1.33x faster                                                    |
| regex_v8       | 27.8 ms                                                | 24.5 ms: 1.13x faster                                                   |
| regex_dna      | 227 ms                                                 | 216 ms: 1.05x faster                                                    |
| regex_effbot   | 3.63 ms                                                | 3.78 ms: 1.04x slower                                                   |
| Geometric mean | (ref)                                                  | 1.11x faster                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241017-linux-x86_64-brandtbucher-justin_unlikely-3.14.0a1+-15229e0 |
|----------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| tomli_loads          | 3.14 sec                                               | 1.91 sec: 1.64x faster                                                  |
| pickle_pure_python   | 484 us                                                 | 309 us: 1.57x faster                                                    |
| unpickle_pure_python | 331 us                                                 | 215 us: 1.53x faster                                                    |
| xml_etree_process    | 79.1 ms                                                | 55.0 ms: 1.44x faster                                                   |
| json_dumps           | 14.2 ms                                                | 10.9 ms: 1.30x faster                                                   |
| xml_etree_generate   | 99.4 ms                                                | 78.5 ms: 1.27x faster                                                   |
| json_loads           | 31.2 us                                                | 26.6 us: 1.17x faster                                                   |
| xml_etree_iterparse  | 115 ms                                                 | 99.1 ms: 1.17x faster                                                   |
| xml_etree_parse      | 168 ms                                                 | 146 ms: 1.15x faster                                                    |
| pickle_list          | 5.08 us                                                | 5.16 us: 1.02x slower                                                   |
| unpickle_list        | 5.20 us                                                | 5.30 us: 1.02x slower                                                   |
| unpickle             | 14.4 us                                                | 14.9 us: 1.04x slower                                                   |
| pickle               | 10.7 us                                                | 11.8 us: 1.11x slower                                                   |
| pickle_dict          | 29.6 us                                                | 35.8 us: 1.21x slower                                                   |
| Geometric mean       | (ref)                                                  | 1.18x faster                                                            |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241017-linux-x86_64-brandtbucher-justin_unlikely-3.14.0a1+-15229e0 |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 11.9 ms: 1.22x faster                                                   |
| python_startup_no_site | 5.93 ms                                                | 7.09 ms: 1.20x slower                                                   |
| Geometric mean         | (ref)                                                  | 1.01x faster                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241017-linux-x86_64-brandtbucher-justin_unlikely-3.14.0a1+-15229e0 |
|-----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mako            | 16.3 ms                                                | 9.93 ms: 1.64x faster                                                   |
| django_template | 48.2 ms                                                | 36.9 ms: 1.31x faster                                                   |
| genshi_text     | 31.8 ms                                                | 25.5 ms: 1.25x faster                                                   |
| genshi_xml      | 66.0 ms                                                | 59.7 ms: 1.11x faster                                                   |
| Geometric mean  | (ref)                                                  | 1.31x faster                                                            |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241017-linux-x86_64-brandtbucher-justin_unlikely-3.14.0a1+-15229e0 |
|--------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 166 us: 3.28x faster                                                    |
| deltablue                | 7.91 ms                                                | 3.26 ms: 2.43x faster                                                   |
| generators               | 80.1 ms                                                | 35.3 ms: 2.27x faster                                                   |
| async_tree_none          | 728 ms                                                 | 328 ms: 2.22x faster                                                    |
| async_tree_memoization   | 870 ms                                                 | 414 ms: 2.10x faster                                                    |
| async_tree_io            | 1.77 sec                                               | 859 ms: 2.06x faster                                                    |
| richards_super           | 94.7 ms                                                | 47.0 ms: 2.01x faster                                                   |
| deepcopy_memo            | 58.5 us                                                | 29.3 us: 2.00x faster                                                   |
| chaos                    | 115 ms                                                 | 57.9 ms: 2.00x faster                                                   |
| richards                 | 79.3 ms                                                | 41.1 ms: 1.93x faster                                                   |
| crypto_pyaes             | 128 ms                                                 | 66.4 ms: 1.93x faster                                                   |
| nbody                    | 154 ms                                                 | 80.9 ms: 1.90x faster                                                   |
| logging_silent           | 190 ns                                                 | 100 ns: 1.90x faster                                                    |
| scimark_sor              | 220 ms                                                 | 118 ms: 1.86x faster                                                    |
| asyncio_tcp              | 922 ms                                                 | 500 ms: 1.85x faster                                                    |
| scimark_monte_carlo      | 118 ms                                                 | 64.1 ms: 1.84x faster                                                   |
| raytrace                 | 507 ms                                                 | 276 ms: 1.83x faster                                                    |
| go                       | 240 ms                                                 | 132 ms: 1.81x faster                                                    |
| deepcopy                 | 479 us                                                 | 270 us: 1.77x faster                                                    |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 574 ms: 1.77x faster                                                    |
| comprehensions           | 28.8 us                                                | 16.9 us: 1.71x faster                                                   |
| mako                     | 16.3 ms                                                | 9.93 ms: 1.64x faster                                                   |
| tomli_loads              | 3.14 sec                                               | 1.91 sec: 1.64x faster                                                  |
| sqlglot_parse            | 2.17 ms                                                | 1.32 ms: 1.64x faster                                                   |
| pyflate                  | 716 ms                                                 | 452 ms: 1.58x faster                                                    |
| pickle_pure_python       | 484 us                                                 | 309 us: 1.57x faster                                                    |
| float                    | 117 ms                                                 | 75.3 ms: 1.56x faster                                                   |
| scimark_lu               | 176 ms                                                 | 113 ms: 1.55x faster                                                    |
| coroutines               | 35.1 ms                                                | 22.8 ms: 1.54x faster                                                   |
| deepcopy_reduce          | 4.17 us                                                | 2.71 us: 1.54x faster                                                   |
| unpickle_pure_python     | 331 us                                                 | 215 us: 1.53x faster                                                    |
| sqlglot_transpile        | 2.57 ms                                                | 1.68 ms: 1.53x faster                                                   |
| hexiom                   | 10.4 ms                                                | 6.98 ms: 1.49x faster                                                   |
| logging_format           | 9.09 us                                                | 6.12 us: 1.48x faster                                                   |
| logging_simple           | 8.30 us                                                | 5.59 us: 1.48x faster                                                   |
| scimark_fft              | 466 ms                                                 | 317 ms: 1.47x faster                                                    |
| pylint                   | 551 ms                                                 | 376 ms: 1.47x faster                                                    |
| spectral_norm            | 170 ms                                                 | 117 ms: 1.45x faster                                                    |
| xml_etree_process        | 79.1 ms                                                | 55.0 ms: 1.44x faster                                                   |
| tornado_http             | 136 ms                                                 | 95.4 ms: 1.43x faster                                                   |
| asyncio_tcp_ssl          | 2.57 sec                                               | 1.80 sec: 1.43x faster                                                  |
| pprint_safe_repr         | 1.02 sec                                               | 719 ms: 1.42x faster                                                    |
| html5lib                 | 88.9 ms                                                | 63.4 ms: 1.40x faster                                                   |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.62 ms: 1.40x faster                                                   |
| pprint_pformat           | 2.10 sec                                               | 1.51 sec: 1.39x faster                                                  |
| thrift                   | 1.07 ms                                                | 783 us: 1.37x faster                                                    |
| fannkuch                 | 532 ms                                                 | 395 ms: 1.35x faster                                                    |
| pycparser                | 1.58 sec                                               | 1.18 sec: 1.34x faster                                                  |
| regex_compile            | 188 ms                                                 | 141 ms: 1.33x faster                                                    |
| django_template          | 48.2 ms                                                | 36.9 ms: 1.31x faster                                                   |
| json_dumps               | 14.2 ms                                                | 10.9 ms: 1.30x faster                                                   |
| pathlib                  | 20.5 ms                                                | 16.1 ms: 1.27x faster                                                   |
| xml_etree_generate       | 99.4 ms                                                | 78.5 ms: 1.27x faster                                                   |
| dulwich_log              | 84.3 ms                                                | 67.0 ms: 1.26x faster                                                   |
| 2to3                     | 348 ms                                                 | 278 ms: 1.26x faster                                                    |
| genshi_text              | 31.8 ms                                                | 25.5 ms: 1.25x faster                                                   |
| sqlglot_normalize        | 143 ms                                                 | 115 ms: 1.25x faster                                                    |
| python_startup           | 14.6 ms                                                | 11.9 ms: 1.22x faster                                                   |
| nqueens                  | 106 ms                                                 | 88.4 ms: 1.20x faster                                                   |
| json_loads               | 31.2 us                                                | 26.6 us: 1.17x faster                                                   |
| xml_etree_iterparse      | 115 ms                                                 | 99.1 ms: 1.17x faster                                                   |
| json                     | 5.69 ms                                                | 4.92 ms: 1.16x faster                                                   |
| sqlglot_optimize         | 69.2 ms                                                | 59.9 ms: 1.15x faster                                                   |
| xml_etree_parse          | 168 ms                                                 | 146 ms: 1.15x faster                                                    |
| sympy_str                | 346 ms                                                 | 301 ms: 1.15x faster                                                    |
| regex_v8                 | 27.8 ms                                                | 24.5 ms: 1.13x faster                                                   |
| sympy_expand             | 566 ms                                                 | 499 ms: 1.13x faster                                                    |
| docutils                 | 3.30 sec                                               | 2.92 sec: 1.13x faster                                                  |
| bench_thread_pool        | 986 us                                                 | 878 us: 1.12x faster                                                    |
| mdp                      | 2.85 sec                                               | 2.54 sec: 1.12x faster                                                  |
| sympy_sum                | 196 ms                                                 | 177 ms: 1.11x faster                                                    |
| genshi_xml               | 66.0 ms                                                | 59.7 ms: 1.11x faster                                                   |
| meteor_contest           | 120 ms                                                 | 109 ms: 1.10x faster                                                    |
| sympy_integrate          | 25.8 ms                                                | 23.5 ms: 1.10x faster                                                   |
| sqlite_synth             | 3.02 us                                                | 2.84 us: 1.07x faster                                                   |
| regex_dna                | 227 ms                                                 | 216 ms: 1.05x faster                                                    |
| pidigits                 | 191 ms                                                 | 187 ms: 1.02x faster                                                    |
| asyncio_websockets       | 559 ms                                                 | 555 ms: 1.01x faster                                                    |
| pickle_list              | 5.08 us                                                | 5.16 us: 1.02x slower                                                   |
| unpickle_list            | 5.20 us                                                | 5.30 us: 1.02x slower                                                   |
| async_generators         | 444 ms                                                 | 461 ms: 1.04x slower                                                    |
| unpickle                 | 14.4 us                                                | 14.9 us: 1.04x slower                                                   |
| regex_effbot             | 3.63 ms                                                | 3.78 ms: 1.04x slower                                                   |
| coverage                 | 79.4 ms                                                | 84.0 ms: 1.06x slower                                                   |
| telco                    | 7.27 ms                                                | 7.79 ms: 1.07x slower                                                   |
| pickle                   | 10.7 us                                                | 11.8 us: 1.11x slower                                                   |
| python_startup_no_site   | 5.93 ms                                                | 7.09 ms: 1.20x slower                                                   |
| pickle_dict              | 29.6 us                                                | 35.8 us: 1.21x slower                                                   |
| gc_traversal             | 3.62 ms                                                | 4.45 ms: 1.23x slower                                                   |
| create_gc_cycles         | 1.62 ms                                                | 2.67 ms: 1.65x slower                                                   |
| unpack_sequence          | 60.0 ns                                                | 106 ns: 1.76x slower                                                    |
| bench_mp_pool            | 24.0 ms                                                | 84.2 ms: 3.51x slower                                                   |
| Geometric mean           | (ref)                                                  | 1.33x faster                                                            |
Ignored benchmarks (9) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (6) of results/bm-20241017-3.14.0a1+-15229e0-JIT/bm-20241017-linux-x86_64-brandtbucher-justin_unlikely-3.14.0a1+-15229e0.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, sphinx

- Geometric mean (including insignificant results): 1.397x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.31x
- 95% likely to have a speedup of 1.29x
- 99% likely to have a speedup of 1.25x

# Memory
- memory change: 1.33x