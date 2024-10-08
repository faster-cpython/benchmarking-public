# Results vs. 3.10.4

- fork: brandtbucher
- ref: justin_compact_exits
- machine: linux-x86_64
- commit hash: cae9e43
- commit date: 2024-09-19
- overall geometric mean: 1.39x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.25x faster
- Memory change: 1.20x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240919-linux-x86_64-brandtbucher-justin_compact_exits-3.14.0a0-cae9e43 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 277 ms: 1.26x faster                                                        |
| docutils       | 3.30 sec                                               | 2.92 sec: 1.13x faster                                                      |
| tornado_http   | 136 ms                                                 | 94.0 ms: 1.45x faster                                                       |
| Geometric mean | (ref)                                                  | 1.27x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240919-linux-x86_64-brandtbucher-justin_compact_exits-3.14.0a0-cae9e43 |
|-------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_memoization  | 870 ms                                                 | 380 ms: 2.29x faster                                                        |
| async_tree_none         | 728 ms                                                 | 320 ms: 2.27x faster                                                        |
| async_tree_io           | 1.77 sec                                               | 929 ms: 1.90x faster                                                        |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 536 ms: 1.89x faster                                                        |
| Geometric mean          | (ref)                                                  | 2.08x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240919-linux-x86_64-brandtbucher-justin_compact_exits-3.14.0a0-cae9e43 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 80.5 ms: 1.91x faster                                                       |
| float          | 117 ms                                                 | 70.4 ms: 1.66x faster                                                       |
| pidigits       | 191 ms                                                 | 186 ms: 1.03x faster                                                        |
| Geometric mean | (ref)                                                  | 1.48x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240919-linux-x86_64-brandtbucher-justin_compact_exits-3.14.0a0-cae9e43 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 137 ms: 1.38x faster                                                        |
| regex_v8       | 27.8 ms                                                | 24.0 ms: 1.15x faster                                                       |
| regex_dna      | 227 ms                                                 | 215 ms: 1.05x faster                                                        |
| Geometric mean | (ref)                                                  | 1.14x faster                                                                |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240919-linux-x86_64-brandtbucher-justin_compact_exits-3.14.0a0-cae9e43 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| tomli_loads          | 3.14 sec                                               | 1.91 sec: 1.64x faster                                                      |
| pickle_pure_python   | 484 us                                                 | 302 us: 1.60x faster                                                        |
| unpickle_pure_python | 331 us                                                 | 213 us: 1.55x faster                                                        |
| xml_etree_process    | 79.1 ms                                                | 53.7 ms: 1.47x faster                                                       |
| json_dumps           | 14.2 ms                                                | 10.2 ms: 1.39x faster                                                       |
| xml_etree_generate   | 99.4 ms                                                | 76.0 ms: 1.31x faster                                                       |
| xml_etree_iterparse  | 115 ms                                                 | 97.4 ms: 1.19x faster                                                       |
| json_loads           | 31.2 us                                                | 27.2 us: 1.15x faster                                                       |
| xml_etree_parse      | 168 ms                                                 | 147 ms: 1.15x faster                                                        |
| pickle_list          | 5.08 us                                                | 5.18 us: 1.02x slower                                                       |
| unpickle             | 14.4 us                                                | 15.0 us: 1.04x slower                                                       |
| pickle               | 10.7 us                                                | 11.5 us: 1.08x slower                                                       |
| pickle_dict          | 29.6 us                                                | 32.9 us: 1.11x slower                                                       |
| Geometric mean       | (ref)                                                  | 1.20x faster                                                                |

Benchmark hidden because not significant (1): unpickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240919-linux-x86_64-brandtbucher-justin_compact_exits-3.14.0a0-cae9e43 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 10.5 ms: 1.38x faster                                                       |
| python_startup_no_site | 5.93 ms                                                | 7.07 ms: 1.19x slower                                                       |
| Geometric mean         | (ref)                                                  | 1.08x faster                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240919-linux-x86_64-brandtbucher-justin_compact_exits-3.14.0a0-cae9e43 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 16.3 ms                                                | 9.72 ms: 1.68x faster                                                       |
| django_template | 48.2 ms                                                | 36.0 ms: 1.34x faster                                                       |
| genshi_text     | 31.8 ms                                                | 24.4 ms: 1.30x faster                                                       |
| genshi_xml      | 66.0 ms                                                | 56.4 ms: 1.17x faster                                                       |
| Geometric mean  | (ref)                                                  | 1.36x faster                                                                |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240919-linux-x86_64-brandtbucher-justin_compact_exits-3.14.0a0-cae9e43 |
|--------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 160 us: 3.41x faster                                                        |
| deltablue                | 7.91 ms                                                | 3.14 ms: 2.52x faster                                                       |
| generators               | 80.1 ms                                                | 32.4 ms: 2.47x faster                                                       |
| async_tree_memoization   | 870 ms                                                 | 380 ms: 2.29x faster                                                        |
| async_tree_none          | 728 ms                                                 | 320 ms: 2.27x faster                                                        |
| deepcopy_memo            | 58.5 us                                                | 26.7 us: 2.19x faster                                                       |
| richards_super           | 94.7 ms                                                | 45.7 ms: 2.07x faster                                                       |
| chaos                    | 115 ms                                                 | 58.4 ms: 1.98x faster                                                       |
| richards                 | 79.3 ms                                                | 40.7 ms: 1.95x faster                                                       |
| crypto_pyaes             | 128 ms                                                 | 66.0 ms: 1.94x faster                                                       |
| go                       | 240 ms                                                 | 125 ms: 1.92x faster                                                        |
| nbody                    | 154 ms                                                 | 80.5 ms: 1.91x faster                                                       |
| async_tree_io            | 1.77 sec                                               | 929 ms: 1.90x faster                                                        |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 536 ms: 1.89x faster                                                        |
| deepcopy                 | 479 us                                                 | 254 us: 1.89x faster                                                        |
| scimark_monte_carlo      | 118 ms                                                 | 62.7 ms: 1.88x faster                                                       |
| scimark_sor              | 220 ms                                                 | 117 ms: 1.88x faster                                                        |
| asyncio_tcp              | 922 ms                                                 | 499 ms: 1.85x faster                                                        |
| raytrace                 | 507 ms                                                 | 275 ms: 1.84x faster                                                        |
| logging_silent           | 190 ns                                                 | 103 ns: 1.84x faster                                                        |
| comprehensions           | 28.8 us                                                | 16.6 us: 1.73x faster                                                       |
| spectral_norm            | 170 ms                                                 | 100 ms: 1.70x faster                                                        |
| mako                     | 16.3 ms                                                | 9.72 ms: 1.68x faster                                                       |
| float                    | 117 ms                                                 | 70.4 ms: 1.66x faster                                                       |
| sqlglot_parse            | 2.17 ms                                                | 1.32 ms: 1.64x faster                                                       |
| tomli_loads              | 3.14 sec                                               | 1.91 sec: 1.64x faster                                                      |
| pickle_pure_python       | 484 us                                                 | 302 us: 1.60x faster                                                        |
| scimark_lu               | 176 ms                                                 | 110 ms: 1.60x faster                                                        |
| pyflate                  | 716 ms                                                 | 457 ms: 1.57x faster                                                        |
| deepcopy_reduce          | 4.17 us                                                | 2.67 us: 1.56x faster                                                       |
| unpickle_pure_python     | 331 us                                                 | 213 us: 1.55x faster                                                        |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.21 ms: 1.54x faster                                                       |
| pylint                   | 551 ms                                                 | 360 ms: 1.53x faster                                                        |
| scimark_fft              | 466 ms                                                 | 306 ms: 1.52x faster                                                        |
| coroutines               | 35.1 ms                                                | 23.1 ms: 1.52x faster                                                       |
| hexiom                   | 10.4 ms                                                | 6.87 ms: 1.51x faster                                                       |
| sqlglot_transpile        | 2.57 ms                                                | 1.70 ms: 1.51x faster                                                       |
| logging_simple           | 8.30 us                                                | 5.57 us: 1.49x faster                                                       |
| logging_format           | 9.09 us                                                | 6.14 us: 1.48x faster                                                       |
| xml_etree_process        | 79.1 ms                                                | 53.7 ms: 1.47x faster                                                       |
| tornado_http             | 136 ms                                                 | 94.0 ms: 1.45x faster                                                       |
| asyncio_tcp_ssl          | 2.57 sec                                               | 1.81 sec: 1.42x faster                                                      |
| pprint_pformat           | 2.10 sec                                               | 1.49 sec: 1.41x faster                                                      |
| pprint_safe_repr         | 1.02 sec                                               | 722 ms: 1.41x faster                                                        |
| fannkuch                 | 532 ms                                                 | 380 ms: 1.40x faster                                                        |
| json_dumps               | 14.2 ms                                                | 10.2 ms: 1.39x faster                                                       |
| python_startup           | 14.6 ms                                                | 10.5 ms: 1.38x faster                                                       |
| regex_compile            | 188 ms                                                 | 137 ms: 1.38x faster                                                        |
| thrift                   | 1.07 ms                                                | 787 us: 1.36x faster                                                        |
| django_template          | 48.2 ms                                                | 36.0 ms: 1.34x faster                                                       |
| xml_etree_generate       | 99.4 ms                                                | 76.0 ms: 1.31x faster                                                       |
| genshi_text              | 31.8 ms                                                | 24.4 ms: 1.30x faster                                                       |
| sqlglot_normalize        | 143 ms                                                 | 110 ms: 1.30x faster                                                        |
| pathlib                  | 20.5 ms                                                | 15.7 ms: 1.30x faster                                                       |
| 2to3                     | 348 ms                                                 | 277 ms: 1.26x faster                                                        |
| dulwich_log              | 84.3 ms                                                | 67.3 ms: 1.25x faster                                                       |
| sqlglot_optimize         | 69.2 ms                                                | 56.5 ms: 1.22x faster                                                       |
| nqueens                  | 106 ms                                                 | 86.8 ms: 1.22x faster                                                       |
| xml_etree_iterparse      | 115 ms                                                 | 97.4 ms: 1.19x faster                                                       |
| bench_thread_pool        | 986 us                                                 | 837 us: 1.18x faster                                                        |
| genshi_xml               | 66.0 ms                                                | 56.4 ms: 1.17x faster                                                       |
| sympy_str                | 346 ms                                                 | 297 ms: 1.16x faster                                                        |
| regex_v8                 | 27.8 ms                                                | 24.0 ms: 1.15x faster                                                       |
| json_loads               | 31.2 us                                                | 27.2 us: 1.15x faster                                                       |
| xml_etree_parse          | 168 ms                                                 | 147 ms: 1.15x faster                                                        |
| sympy_sum                | 196 ms                                                 | 171 ms: 1.15x faster                                                        |
| sympy_integrate          | 25.8 ms                                                | 22.7 ms: 1.14x faster                                                       |
| mdp                      | 2.85 sec                                               | 2.52 sec: 1.13x faster                                                      |
| docutils                 | 3.30 sec                                               | 2.92 sec: 1.13x faster                                                      |
| sympy_expand             | 566 ms                                                 | 502 ms: 1.13x faster                                                        |
| meteor_contest           | 120 ms                                                 | 107 ms: 1.12x faster                                                        |
| json                     | 5.69 ms                                                | 5.09 ms: 1.12x faster                                                       |
| sqlite_synth             | 3.02 us                                                | 2.73 us: 1.11x faster                                                       |
| regex_dna                | 227 ms                                                 | 215 ms: 1.05x faster                                                        |
| pidigits                 | 191 ms                                                 | 186 ms: 1.03x faster                                                        |
| asyncio_websockets       | 559 ms                                                 | 555 ms: 1.01x faster                                                        |
| pickle_list              | 5.08 us                                                | 5.18 us: 1.02x slower                                                       |
| gc_traversal             | 3.62 ms                                                | 3.72 ms: 1.03x slower                                                       |
| async_generators         | 444 ms                                                 | 458 ms: 1.03x slower                                                        |
| unpickle                 | 14.4 us                                                | 15.0 us: 1.04x slower                                                       |
| coverage                 | 79.4 ms                                                | 84.7 ms: 1.07x slower                                                       |
| create_gc_cycles         | 1.62 ms                                                | 1.74 ms: 1.07x slower                                                       |
| pickle                   | 10.7 us                                                | 11.5 us: 1.08x slower                                                       |
| telco                    | 7.27 ms                                                | 7.95 ms: 1.09x slower                                                       |
| pickle_dict              | 29.6 us                                                | 32.9 us: 1.11x slower                                                       |
| python_startup_no_site   | 5.93 ms                                                | 7.07 ms: 1.19x slower                                                       |
| unpack_sequence          | 60.0 ns                                                | 109 ns: 1.81x slower                                                        |
| Geometric mean           | (ref)                                                  | 1.39x faster                                                                |

Benchmark hidden because not significant (3): unpickle_list, bench_mp_pool, regex_effbot
Ignored benchmarks (11) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, djangocms, flaskblogging, gunicorn, html5lib, mypy2, pycparser, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (5) of results/bm-20240919-3.14.0a0-cae9e43-JIT/bm-20240919-linux-x86_64-brandtbucher-justin_compact_exits-3.14.0a0-cae9e43.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.32x
- 95% likely to have a speedup of 1.30x
- 99% likely to have a speedup of 1.25x

# Memory
- memory change: 1.20x