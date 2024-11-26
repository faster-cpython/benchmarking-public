# Results vs. 3.10.4

- fork: faster-cpython
- ref: immortal_ref_count_s
- machine: linux-x86_64
- commit hash: e179c31
- commit date: 2024-09-20
- overall geometric mean: 1.436x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.31x faster
- Memory change: 1.12x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240920-linux-x86_64-faster%2dcpython-immortal_ref_count_s-3.14.0a0-e179c31 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 255 ms: 1.37x faster                                                            |
| docutils       | 3.30 sec                                               | 2.65 sec: 1.24x faster                                                          |
| html5lib       | 88.9 ms                                                | 62.2 ms: 1.43x faster                                                           |
| tornado_http   | 136 ms                                                 | 89.8 ms: 1.52x faster                                                           |
| Geometric mean | (ref)                                                  | 1.39x faster                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240920-linux-x86_64-faster%2dcpython-immortal_ref_count_s-3.14.0a0-e179c31 |
|-------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_none         | 728 ms                                                 | 310 ms: 2.35x faster                                                            |
| async_tree_memoization  | 870 ms                                                 | 391 ms: 2.22x faster                                                            |
| async_tree_io           | 1.77 sec                                               | 856 ms: 2.07x faster                                                            |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 563 ms: 1.80x faster                                                            |
| Geometric mean          | (ref)                                                  | 2.10x faster                                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240920-linux-x86_64-faster%2dcpython-immortal_ref_count_s-3.14.0a0-e179c31 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 89.9 ms: 1.71x faster                                                           |
| float          | 117 ms                                                 | 76.6 ms: 1.53x faster                                                           |
| pidigits       | 191 ms                                                 | 186 ms: 1.02x faster                                                            |
| Geometric mean | (ref)                                                  | 1.39x faster                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240920-linux-x86_64-faster%2dcpython-immortal_ref_count_s-3.14.0a0-e179c31 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 127 ms: 1.48x faster                                                            |
| regex_v8       | 27.8 ms                                                | 24.7 ms: 1.12x faster                                                           |
| regex_dna      | 227 ms                                                 | 225 ms: 1.01x faster                                                            |
| Geometric mean | (ref)                                                  | 1.13x faster                                                                    |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240920-linux-x86_64-faster%2dcpython-immortal_ref_count_s-3.14.0a0-e179c31 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| pickle_pure_python   | 484 us                                                 | 304 us: 1.59x faster                                                            |
| unpickle_pure_python | 331 us                                                 | 214 us: 1.54x faster                                                            |
| tomli_loads          | 3.14 sec                                               | 2.10 sec: 1.50x faster                                                          |
| json_dumps           | 14.2 ms                                                | 10.1 ms: 1.40x faster                                                           |
| xml_etree_process    | 79.1 ms                                                | 58.7 ms: 1.35x faster                                                           |
| xml_etree_generate   | 99.4 ms                                                | 84.8 ms: 1.17x faster                                                           |
| json_loads           | 31.2 us                                                | 26.8 us: 1.16x faster                                                           |
| xml_etree_iterparse  | 115 ms                                                 | 105 ms: 1.10x faster                                                            |
| xml_etree_parse      | 168 ms                                                 | 154 ms: 1.09x faster                                                            |
| unpickle_list        | 5.20 us                                                | 5.27 us: 1.01x slower                                                           |
| pickle_list          | 5.08 us                                                | 5.18 us: 1.02x slower                                                           |
| pickle               | 10.7 us                                                | 11.7 us: 1.10x slower                                                           |
| unpickle             | 14.4 us                                                | 16.0 us: 1.11x slower                                                           |
| pickle_dict          | 29.6 us                                                | 35.4 us: 1.20x slower                                                           |
| Geometric mean       | (ref)                                                  | 1.15x faster                                                                    |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240920-linux-x86_64-faster%2dcpython-immortal_ref_count_s-3.14.0a0-e179c31 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 10.5 ms: 1.39x faster                                                           |
| python_startup_no_site | 5.93 ms                                                | 7.00 ms: 1.18x slower                                                           |
| Geometric mean         | (ref)                                                  | 1.09x faster                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240920-linux-x86_64-faster%2dcpython-immortal_ref_count_s-3.14.0a0-e179c31 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| genshi_text     | 31.8 ms                                                | 21.9 ms: 1.45x faster                                                           |
| mako            | 16.3 ms                                                | 11.4 ms: 1.44x faster                                                           |
| django_template | 48.2 ms                                                | 34.5 ms: 1.40x faster                                                           |
| genshi_xml      | 66.0 ms                                                | 49.2 ms: 1.34x faster                                                           |
| Geometric mean  | (ref)                                                  | 1.41x faster                                                                    |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240920-linux-x86_64-faster%2dcpython-immortal_ref_count_s-3.14.0a0-e179c31 |
|--------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 157 us: 3.47x faster                                                            |
| generators               | 80.1 ms                                                | 27.9 ms: 2.87x faster                                                           |
| deltablue                | 7.91 ms                                                | 3.28 ms: 2.41x faster                                                           |
| async_tree_none          | 728 ms                                                 | 310 ms: 2.35x faster                                                            |
| async_tree_memoization   | 870 ms                                                 | 391 ms: 2.22x faster                                                            |
| async_tree_io            | 1.77 sec                                               | 856 ms: 2.07x faster                                                            |
| go                       | 240 ms                                                 | 120 ms: 2.00x faster                                                            |
| asyncio_tcp              | 922 ms                                                 | 468 ms: 1.97x faster                                                            |
| chaos                    | 115 ms                                                 | 59.0 ms: 1.96x faster                                                           |
| deepcopy_memo            | 58.5 us                                                | 30.4 us: 1.92x faster                                                           |
| raytrace                 | 507 ms                                                 | 265 ms: 1.91x faster                                                            |
| deepcopy                 | 479 us                                                 | 256 us: 1.87x faster                                                            |
| logging_silent           | 190 ns                                                 | 104 ns: 1.83x faster                                                            |
| richards_super           | 94.7 ms                                                | 52.3 ms: 1.81x faster                                                           |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 563 ms: 1.80x faster                                                            |
| crypto_pyaes             | 128 ms                                                 | 71.0 ms: 1.80x faster                                                           |
| scimark_sor              | 220 ms                                                 | 124 ms: 1.77x faster                                                            |
| scimark_monte_carlo      | 118 ms                                                 | 67.7 ms: 1.75x faster                                                           |
| comprehensions           | 28.8 us                                                | 16.5 us: 1.74x faster                                                           |
| pylint                   | 551 ms                                                 | 319 ms: 1.73x faster                                                            |
| nbody                    | 154 ms                                                 | 89.9 ms: 1.71x faster                                                           |
| richards                 | 79.3 ms                                                | 46.5 ms: 1.70x faster                                                           |
| sqlglot_parse            | 2.17 ms                                                | 1.28 ms: 1.70x faster                                                           |
| hexiom                   | 10.4 ms                                                | 6.20 ms: 1.68x faster                                                           |
| sqlglot_transpile        | 2.57 ms                                                | 1.58 ms: 1.63x faster                                                           |
| pickle_pure_python       | 484 us                                                 | 304 us: 1.59x faster                                                            |
| scimark_lu               | 176 ms                                                 | 112 ms: 1.57x faster                                                            |
| deepcopy_reduce          | 4.17 us                                                | 2.67 us: 1.56x faster                                                           |
| unpickle_pure_python     | 331 us                                                 | 214 us: 1.54x faster                                                            |
| pyflate                  | 716 ms                                                 | 468 ms: 1.53x faster                                                            |
| float                    | 117 ms                                                 | 76.6 ms: 1.53x faster                                                           |
| tornado_http             | 136 ms                                                 | 89.8 ms: 1.52x faster                                                           |
| spectral_norm            | 170 ms                                                 | 113 ms: 1.50x faster                                                            |
| coroutines               | 35.1 ms                                                | 23.4 ms: 1.50x faster                                                           |
| tomli_loads              | 3.14 sec                                               | 2.10 sec: 1.50x faster                                                          |
| logging_simple           | 8.30 us                                                | 5.59 us: 1.49x faster                                                           |
| regex_compile            | 188 ms                                                 | 127 ms: 1.48x faster                                                            |
| logging_format           | 9.09 us                                                | 6.19 us: 1.47x faster                                                           |
| genshi_text              | 31.8 ms                                                | 21.9 ms: 1.45x faster                                                           |
| pprint_pformat           | 2.10 sec                                               | 1.46 sec: 1.44x faster                                                          |
| asyncio_tcp_ssl          | 2.57 sec                                               | 1.79 sec: 1.44x faster                                                          |
| mako                     | 16.3 ms                                                | 11.4 ms: 1.44x faster                                                           |
| pprint_safe_repr         | 1.02 sec                                               | 710 ms: 1.43x faster                                                            |
| html5lib                 | 88.9 ms                                                | 62.2 ms: 1.43x faster                                                           |
| thrift                   | 1.07 ms                                                | 763 us: 1.40x faster                                                            |
| json_dumps               | 14.2 ms                                                | 10.1 ms: 1.40x faster                                                           |
| django_template          | 48.2 ms                                                | 34.5 ms: 1.40x faster                                                           |
| python_startup           | 14.6 ms                                                | 10.5 ms: 1.39x faster                                                           |
| 2to3                     | 348 ms                                                 | 255 ms: 1.37x faster                                                            |
| sqlglot_normalize        | 143 ms                                                 | 106 ms: 1.35x faster                                                            |
| pycparser                | 1.58 sec                                               | 1.17 sec: 1.35x faster                                                          |
| xml_etree_process        | 79.1 ms                                                | 58.7 ms: 1.35x faster                                                           |
| sympy_sum                | 196 ms                                                 | 146 ms: 1.34x faster                                                            |
| genshi_xml               | 66.0 ms                                                | 49.2 ms: 1.34x faster                                                           |
| nqueens                  | 106 ms                                                 | 78.9 ms: 1.34x faster                                                           |
| sympy_integrate          | 25.8 ms                                                | 19.5 ms: 1.32x faster                                                           |
| fannkuch                 | 532 ms                                                 | 404 ms: 1.31x faster                                                            |
| dulwich_log              | 84.3 ms                                                | 64.3 ms: 1.31x faster                                                           |
| sqlglot_optimize         | 69.2 ms                                                | 52.9 ms: 1.31x faster                                                           |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.96 ms: 1.30x faster                                                           |
| sympy_str                | 346 ms                                                 | 268 ms: 1.29x faster                                                            |
| unpack_sequence          | 60.0 ns                                                | 46.4 ns: 1.29x faster                                                           |
| pathlib                  | 20.5 ms                                                | 16.1 ms: 1.27x faster                                                           |
| scimark_fft              | 466 ms                                                 | 367 ms: 1.27x faster                                                            |
| bench_thread_pool        | 986 us                                                 | 791 us: 1.25x faster                                                            |
| docutils                 | 3.30 sec                                               | 2.65 sec: 1.24x faster                                                          |
| sympy_expand             | 566 ms                                                 | 456 ms: 1.24x faster                                                            |
| xml_etree_generate       | 99.4 ms                                                | 84.8 ms: 1.17x faster                                                           |
| json                     | 5.69 ms                                                | 4.86 ms: 1.17x faster                                                           |
| json_loads               | 31.2 us                                                | 26.8 us: 1.16x faster                                                           |
| regex_v8                 | 27.8 ms                                                | 24.7 ms: 1.12x faster                                                           |
| meteor_contest           | 120 ms                                                 | 107 ms: 1.12x faster                                                            |
| xml_etree_iterparse      | 115 ms                                                 | 105 ms: 1.10x faster                                                            |
| xml_etree_parse          | 168 ms                                                 | 154 ms: 1.09x faster                                                            |
| sqlite_synth             | 3.02 us                                                | 2.85 us: 1.06x faster                                                           |
| mdp                      | 2.85 sec                                               | 2.69 sec: 1.06x faster                                                          |
| async_generators         | 444 ms                                                 | 432 ms: 1.03x faster                                                            |
| pidigits                 | 191 ms                                                 | 186 ms: 1.02x faster                                                            |
| gc_traversal             | 3.62 ms                                                | 3.55 ms: 1.02x faster                                                           |
| regex_dna                | 227 ms                                                 | 225 ms: 1.01x faster                                                            |
| unpickle_list            | 5.20 us                                                | 5.27 us: 1.01x slower                                                           |
| pickle_list              | 5.08 us                                                | 5.18 us: 1.02x slower                                                           |
| create_gc_cycles         | 1.62 ms                                                | 1.73 ms: 1.07x slower                                                           |
| coverage                 | 79.4 ms                                                | 86.8 ms: 1.09x slower                                                           |
| pickle                   | 10.7 us                                                | 11.7 us: 1.10x slower                                                           |
| unpickle                 | 14.4 us                                                | 16.0 us: 1.11x slower                                                           |
| telco                    | 7.27 ms                                                | 8.51 ms: 1.17x slower                                                           |
| python_startup_no_site   | 5.93 ms                                                | 7.00 ms: 1.18x slower                                                           |
| pickle_dict              | 29.6 us                                                | 35.4 us: 1.20x slower                                                           |
| Geometric mean           | (ref)                                                  | 1.40x faster                                                                    |

Benchmark hidden because not significant (3): asyncio_websockets, bench_mp_pool, regex_effbot
Ignored benchmarks (9) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (5) of results/bm-20240920-3.14.0a0-e179c31/bm-20240920-linux-x86_64-faster%2dcpython-immortal_ref_count_s-3.14.0a0-e179c31.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

- Geometric mean (including insignificant results): 1.436x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.34x
- 95% likely to have a speedup of 1.33x
- 99% likely to have a speedup of 1.31x

# Memory
- memory change: 1.12x