# Results vs. 3.10.4

- fork: python
- ref: fba5dded6df3c2b19435
- machine: linux-x86_64
- commit hash: fba5dde
- commit date: 2025-06-17
- overall geometric mean: 1.076x faster
- HPT reliability: 98.65%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.59x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250617-linux-x86_64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 339 ms: 1.03x faster                                                  |
| docutils       | 3.30 sec                                               | 3.16 sec: 1.04x faster                                                |
| html5lib       | 88.9 ms                                                | 75.4 ms: 1.18x faster                                                 |
| Geometric mean | (ref)                                                  | 1.08x faster                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250617-linux-x86_64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|-------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_io           | 1.77 sec                                               | 633 ms: 2.79x faster                                                  |
| async_tree_none         | 728 ms                                                 | 299 ms: 2.44x faster                                                  |
| async_tree_memoization  | 870 ms                                                 | 375 ms: 2.32x faster                                                  |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 610 ms: 1.67x faster                                                  |
| Geometric mean          | (ref)                                                  | 2.27x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250617-linux-x86_64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 117 ms                                                 | 81.1 ms: 1.44x faster                                                 |
| nbody          | 154 ms                                                 | 151 ms: 1.01x faster                                                  |
| pidigits       | 191 ms                                                 | 203 ms: 1.06x slower                                                  |
| Geometric mean | (ref)                                                  | 1.11x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250617-linux-x86_64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_effbot   | 3.63 ms                                                | 2.99 ms: 1.21x faster                                                 |
| regex_dna      | 227 ms                                                 | 192 ms: 1.18x faster                                                  |
| regex_v8       | 27.8 ms                                                | 23.6 ms: 1.17x faster                                                 |
| regex_compile  | 188 ms                                                 | 172 ms: 1.10x faster                                                  |
| Geometric mean | (ref)                                                  | 1.17x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250617-linux-x86_64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| tomli_loads          | 3.14 sec                                               | 2.63 sec: 1.19x faster                                                |
| pickle_pure_python   | 484 us                                                 | 424 us: 1.14x faster                                                  |
| unpickle_pure_python | 331 us                                                 | 296 us: 1.12x faster                                                  |
| xml_etree_iterparse  | 115 ms                                                 | 108 ms: 1.07x faster                                                  |
| xml_etree_parse      | 168 ms                                                 | 165 ms: 1.02x faster                                                  |
| json_dumps           | 14.2 ms                                                | 14.8 ms: 1.04x slower                                                 |
| xml_etree_process    | 79.1 ms                                                | 87.5 ms: 1.11x slower                                                 |
| pickle_list          | 5.08 us                                                | 5.91 us: 1.16x slower                                                 |
| json_loads           | 31.2 us                                                | 37.2 us: 1.19x slower                                                 |
| unpickle_list        | 5.20 us                                                | 6.40 us: 1.23x slower                                                 |
| xml_etree_generate   | 99.4 ms                                                | 125 ms: 1.25x slower                                                  |
| pickle_dict          | 29.6 us                                                | 37.4 us: 1.26x slower                                                 |
| pickle               | 10.7 us                                                | 15.4 us: 1.44x slower                                                 |
| unpickle             | 14.4 us                                                | 22.2 us: 1.54x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.11x slower                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250617-linux-x86_64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 17.2 ms: 1.18x slower                                                 |
| python_startup_no_site | 5.93 ms                                                | 10.0 ms: 1.69x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.41x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250617-linux-x86_64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| django_template | 48.2 ms                                                | 53.5 ms: 1.11x slower                                                 |
| genshi_text     | 31.8 ms                                                | 35.5 ms: 1.11x slower                                                 |
| mako            | 16.3 ms                                                | 18.9 ms: 1.16x slower                                                 |
| genshi_xml      | 66.0 ms                                                | 77.5 ms: 1.17x slower                                                 |
| Geometric mean  | (ref)                                                  | 1.14x slower                                                          |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250617-linux-x86_64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|--------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_io            | 1.77 sec                                               | 633 ms: 2.79x faster                                                  |
| async_tree_none          | 728 ms                                                 | 299 ms: 2.44x faster                                                  |
| async_tree_memoization   | 870 ms                                                 | 375 ms: 2.32x faster                                                  |
| typing_runtime_protocols | 544 us                                                 | 238 us: 2.28x faster                                                  |
| generators               | 80.1 ms                                                | 35.1 ms: 2.28x faster                                                 |
| deltablue                | 7.91 ms                                                | 4.56 ms: 1.73x faster                                                 |
| go                       | 240 ms                                                 | 139 ms: 1.73x faster                                                  |
| asyncio_tcp              | 922 ms                                                 | 549 ms: 1.68x faster                                                  |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 610 ms: 1.67x faster                                                  |
| mdp                      | 2.85 sec                                               | 1.74 sec: 1.64x faster                                                |
| pylint                   | 551 ms                                                 | 357 ms: 1.55x faster                                                  |
| float                    | 117 ms                                                 | 81.1 ms: 1.44x faster                                                 |
| deepcopy_memo            | 58.5 us                                                | 40.8 us: 1.43x faster                                                 |
| chaos                    | 115 ms                                                 | 81.4 ms: 1.42x faster                                                 |
| scimark_sor              | 220 ms                                                 | 156 ms: 1.41x faster                                                  |
| hexiom                   | 10.4 ms                                                | 7.90 ms: 1.32x faster                                                 |
| raytrace                 | 507 ms                                                 | 387 ms: 1.31x faster                                                  |
| pyflate                  | 716 ms                                                 | 550 ms: 1.30x faster                                                  |
| deepcopy                 | 479 us                                                 | 378 us: 1.27x faster                                                  |
| asyncio_tcp_ssl          | 2.57 sec                                               | 2.03 sec: 1.26x faster                                                |
| comprehensions           | 28.8 us                                                | 22.9 us: 1.26x faster                                                 |
| gc_traversal             | 3.62 ms                                                | 2.89 ms: 1.25x faster                                                 |
| spectral_norm            | 170 ms                                                 | 137 ms: 1.24x faster                                                  |
| richards_super           | 94.7 ms                                                | 77.4 ms: 1.22x faster                                                 |
| pycparser                | 1.58 sec                                               | 1.29 sec: 1.22x faster                                                |
| coroutines               | 35.1 ms                                                | 28.8 ms: 1.22x faster                                                 |
| regex_effbot             | 3.63 ms                                                | 2.99 ms: 1.21x faster                                                 |
| tomli_loads              | 3.14 sec                                               | 2.63 sec: 1.19x faster                                                |
| richards                 | 79.3 ms                                                | 66.9 ms: 1.19x faster                                                 |
| scimark_monte_carlo      | 118 ms                                                 | 99.8 ms: 1.18x faster                                                 |
| regex_dna                | 227 ms                                                 | 192 ms: 1.18x faster                                                  |
| html5lib                 | 88.9 ms                                                | 75.4 ms: 1.18x faster                                                 |
| regex_v8                 | 27.8 ms                                                | 23.6 ms: 1.17x faster                                                 |
| dulwich_log              | 84.3 ms                                                | 73.0 ms: 1.15x faster                                                 |
| crypto_pyaes             | 128 ms                                                 | 112 ms: 1.14x faster                                                  |
| pickle_pure_python       | 484 us                                                 | 424 us: 1.14x faster                                                  |
| unpickle_pure_python     | 331 us                                                 | 296 us: 1.12x faster                                                  |
| regex_compile            | 188 ms                                                 | 172 ms: 1.10x faster                                                  |
| scimark_lu               | 176 ms                                                 | 161 ms: 1.09x faster                                                  |
| xml_etree_iterparse      | 115 ms                                                 | 108 ms: 1.07x faster                                                  |
| unpack_sequence          | 60.0 ns                                                | 56.9 ns: 1.05x faster                                                 |
| docutils                 | 3.30 sec                                               | 3.16 sec: 1.04x faster                                                |
| pathlib                  | 20.5 ms                                                | 19.7 ms: 1.04x faster                                                 |
| 2to3                     | 348 ms                                                 | 339 ms: 1.03x faster                                                  |
| sympy_integrate          | 25.8 ms                                                | 25.2 ms: 1.02x faster                                                 |
| xml_etree_parse          | 168 ms                                                 | 165 ms: 1.02x faster                                                  |
| nbody                    | 154 ms                                                 | 151 ms: 1.01x faster                                                  |
| asyncio_websockets       | 559 ms                                                 | 552 ms: 1.01x faster                                                  |
| sympy_sum                | 196 ms                                                 | 199 ms: 1.01x slower                                                  |
| async_generators         | 444 ms                                                 | 452 ms: 1.02x slower                                                  |
| scimark_fft              | 466 ms                                                 | 479 ms: 1.03x slower                                                  |
| json_dumps               | 14.2 ms                                                | 14.8 ms: 1.04x slower                                                 |
| pidigits                 | 191 ms                                                 | 203 ms: 1.06x slower                                                  |
| sqlite_synth             | 3.02 us                                                | 3.21 us: 1.06x slower                                                 |
| sympy_str                | 346 ms                                                 | 369 ms: 1.07x slower                                                  |
| fannkuch                 | 532 ms                                                 | 573 ms: 1.08x slower                                                  |
| logging_simple           | 8.30 us                                                | 9.09 us: 1.09x slower                                                 |
| thrift                   | 1.07 ms                                                | 1.18 ms: 1.10x slower                                                 |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 7.11 ms: 1.10x slower                                                 |
| nqueens                  | 106 ms                                                 | 116 ms: 1.10x slower                                                  |
| xml_etree_process        | 79.1 ms                                                | 87.5 ms: 1.11x slower                                                 |
| django_template          | 48.2 ms                                                | 53.5 ms: 1.11x slower                                                 |
| sympy_expand             | 566 ms                                                 | 630 ms: 1.11x slower                                                  |
| genshi_text              | 31.8 ms                                                | 35.5 ms: 1.11x slower                                                 |
| logging_format           | 9.09 us                                                | 10.2 us: 1.12x slower                                                 |
| pprint_pformat           | 2.10 sec                                               | 2.38 sec: 1.13x slower                                                |
| pprint_safe_repr         | 1.02 sec                                               | 1.15 sec: 1.13x slower                                                |
| meteor_contest           | 120 ms                                                 | 137 ms: 1.15x slower                                                  |
| create_gc_cycles         | 1.62 ms                                                | 1.88 ms: 1.16x slower                                                 |
| mako                     | 16.3 ms                                                | 18.9 ms: 1.16x slower                                                 |
| pickle_list              | 5.08 us                                                | 5.91 us: 1.16x slower                                                 |
| json                     | 5.69 ms                                                | 6.62 ms: 1.16x slower                                                 |
| genshi_xml               | 66.0 ms                                                | 77.5 ms: 1.17x slower                                                 |
| python_startup           | 14.6 ms                                                | 17.2 ms: 1.18x slower                                                 |
| json_loads               | 31.2 us                                                | 37.2 us: 1.19x slower                                                 |
| unpickle_list            | 5.20 us                                                | 6.40 us: 1.23x slower                                                 |
| xml_etree_generate       | 99.4 ms                                                | 125 ms: 1.25x slower                                                  |
| pickle_dict              | 29.6 us                                                | 37.4 us: 1.26x slower                                                 |
| pickle                   | 10.7 us                                                | 15.4 us: 1.44x slower                                                 |
| unpickle                 | 14.4 us                                                | 22.2 us: 1.54x slower                                                 |
| coverage                 | 79.4 ms                                                | 128 ms: 1.61x slower                                                  |
| telco                    | 7.27 ms                                                | 12.1 ms: 1.66x slower                                                 |
| python_startup_no_site   | 5.93 ms                                                | 10.0 ms: 1.69x slower                                                 |
| bench_thread_pool        | 986 us                                                 | 3.51 ms: 3.56x slower                                                 |
| logging_silent           | 190 ns                                                 | 755 ns: 3.98x slower                                                  |
| bench_mp_pool            | 24.0 ms                                                | 112 ms: 4.67x slower                                                  |
| Geometric mean           | (ref)                                                  | 1.04x faster                                                          |

Benchmark hidden because not significant (1): deepcopy_reduce
Ignored benchmarks (14) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (15) of results/bm-20250617-3.15.0a0-fba5dde-NOGIL/bm-20250617-linux-x86_64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.076x faster

# HPT report

- Reliability score: 98.65% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.59x