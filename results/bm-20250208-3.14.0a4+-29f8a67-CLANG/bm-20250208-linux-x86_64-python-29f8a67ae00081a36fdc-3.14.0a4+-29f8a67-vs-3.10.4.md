# Results vs. 3.10.4

- fork: python
- ref: 29f8a67ae00081a36fdc
- machine: linux-x86_64
- commit hash: 29f8a67
- commit date: 2025-02-08
- overall geometric mean: 1.503x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.37x faster
- Memory change: 1.27x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250208-linux-x86_64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 247 ms: 1.41x faster                                                   |
| docutils       | 3.30 sec                                               | 2.56 sec: 1.29x faster                                                 |
| html5lib       | 88.9 ms                                                | 60.3 ms: 1.47x faster                                                  |
| Geometric mean | (ref)                                                  | 1.39x faster                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250208-linux-x86_64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|-------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_io           | 1.77 sec                                               | 605 ms: 2.92x faster                                                   |
| async_tree_none         | 728 ms                                                 | 254 ms: 2.86x faster                                                   |
| async_tree_memoization  | 870 ms                                                 | 310 ms: 2.80x faster                                                   |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 528 ms: 1.93x faster                                                   |
| Geometric mean          | (ref)                                                  | 2.59x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250208-linux-x86_64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 81.8 ms: 1.88x faster                                                  |
| float          | 117 ms                                                 | 65.4 ms: 1.79x faster                                                  |
| pidigits       | 191 ms                                                 | 212 ms: 1.11x slower                                                   |
| Geometric mean | (ref)                                                  | 1.45x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250208-linux-x86_64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 123 ms: 1.53x faster                                                   |
| regex_dna      | 227 ms                                                 | 197 ms: 1.15x faster                                                   |
| regex_effbot   | 3.63 ms                                                | 3.20 ms: 1.13x faster                                                  |
| regex_v8       | 27.8 ms                                                | 25.2 ms: 1.10x faster                                                  |
| Geometric mean | (ref)                                                  | 1.22x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250208-linux-x86_64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| tomli_loads          | 3.14 sec                                               | 1.90 sec: 1.65x faster                                                 |
| pickle_pure_python   | 484 us                                                 | 302 us: 1.60x faster                                                   |
| unpickle_pure_python | 331 us                                                 | 213 us: 1.55x faster                                                   |
| xml_etree_process    | 79.1 ms                                                | 57.5 ms: 1.38x faster                                                  |
| xml_etree_generate   | 99.4 ms                                                | 84.6 ms: 1.18x faster                                                  |
| json_dumps           | 14.2 ms                                                | 12.2 ms: 1.16x faster                                                  |
| xml_etree_iterparse  | 115 ms                                                 | 99.7 ms: 1.16x faster                                                  |
| xml_etree_parse      | 168 ms                                                 | 156 ms: 1.08x faster                                                   |
| json_loads           | 31.2 us                                                | 30.2 us: 1.03x faster                                                  |
| Geometric mean       | (ref)                                                  | 1.29x faster                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250208-linux-x86_64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 12.6 ms: 1.15x faster                                                  |
| python_startup_no_site | 5.93 ms                                                | 6.96 ms: 1.17x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.01x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250208-linux-x86_64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| django_template | 48.2 ms                                                | 30.3 ms: 1.59x faster                                                  |
| genshi_text     | 31.8 ms                                                | 20.5 ms: 1.55x faster                                                  |
| mako            | 16.3 ms                                                | 11.5 ms: 1.42x faster                                                  |
| genshi_xml      | 66.0 ms                                                | 47.6 ms: 1.39x faster                                                  |
| Geometric mean  | (ref)                                                  | 1.49x faster                                                           |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250208-linux-x86_64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|--------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 150 us: 3.63x faster                                                   |
| async_tree_io            | 1.77 sec                                               | 605 ms: 2.92x faster                                                   |
| generators               | 80.1 ms                                                | 27.6 ms: 2.90x faster                                                  |
| async_tree_none          | 728 ms                                                 | 254 ms: 2.86x faster                                                   |
| async_tree_memoization   | 870 ms                                                 | 310 ms: 2.80x faster                                                   |
| deltablue                | 7.91 ms                                                | 3.03 ms: 2.61x faster                                                  |
| chaos                    | 115 ms                                                 | 54.4 ms: 2.12x faster                                                  |
| go                       | 240 ms                                                 | 113 ms: 2.12x faster                                                   |
| logging_silent           | 190 ns                                                 | 91.1 ns: 2.08x faster                                                  |
| pylint                   | 551 ms                                                 | 269 ms: 2.05x faster                                                   |
| deepcopy_memo            | 58.5 us                                                | 28.6 us: 2.04x faster                                                  |
| spectral_norm            | 170 ms                                                 | 84.5 ms: 2.01x faster                                                  |
| scimark_sor              | 220 ms                                                 | 110 ms: 2.00x faster                                                   |
| richards_super           | 94.7 ms                                                | 47.6 ms: 1.99x faster                                                  |
| scimark_monte_carlo      | 118 ms                                                 | 59.4 ms: 1.99x faster                                                  |
| raytrace                 | 507 ms                                                 | 257 ms: 1.97x faster                                                   |
| deepcopy                 | 479 us                                                 | 245 us: 1.95x faster                                                   |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 528 ms: 1.93x faster                                                   |
| richards                 | 79.3 ms                                                | 41.2 ms: 1.92x faster                                                  |
| comprehensions           | 28.8 us                                                | 15.1 us: 1.91x faster                                                  |
| nbody                    | 154 ms                                                 | 81.8 ms: 1.88x faster                                                  |
| crypto_pyaes             | 128 ms                                                 | 68.5 ms: 1.86x faster                                                  |
| sqlglot_parse            | 2.17 ms                                                | 1.18 ms: 1.84x faster                                                  |
| float                    | 117 ms                                                 | 65.4 ms: 1.79x faster                                                  |
| pyflate                  | 716 ms                                                 | 405 ms: 1.77x faster                                                   |
| hexiom                   | 10.4 ms                                                | 5.91 ms: 1.76x faster                                                  |
| sqlglot_transpile        | 2.57 ms                                                | 1.48 ms: 1.74x faster                                                  |
| tomli_loads              | 3.14 sec                                               | 1.90 sec: 1.65x faster                                                 |
| deepcopy_reduce          | 4.17 us                                                | 2.56 us: 1.63x faster                                                  |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.02 ms: 1.61x faster                                                  |
| coroutines               | 35.1 ms                                                | 21.8 ms: 1.61x faster                                                  |
| scimark_lu               | 176 ms                                                 | 110 ms: 1.60x faster                                                   |
| pickle_pure_python       | 484 us                                                 | 302 us: 1.60x faster                                                   |
| scimark_fft              | 466 ms                                                 | 292 ms: 1.60x faster                                                   |
| django_template          | 48.2 ms                                                | 30.3 ms: 1.59x faster                                                  |
| logging_simple           | 8.30 us                                                | 5.30 us: 1.57x faster                                                  |
| logging_format           | 9.09 us                                                | 5.84 us: 1.56x faster                                                  |
| genshi_text              | 31.8 ms                                                | 20.5 ms: 1.55x faster                                                  |
| unpickle_pure_python     | 331 us                                                 | 213 us: 1.55x faster                                                   |
| regex_compile            | 188 ms                                                 | 123 ms: 1.53x faster                                                   |
| html5lib                 | 88.9 ms                                                | 60.3 ms: 1.47x faster                                                  |
| sqlalchemy_imperative    | 23.3 ms                                                | 15.9 ms: 1.47x faster                                                  |
| thrift                   | 1.07 ms                                                | 742 us: 1.44x faster                                                   |
| nqueens                  | 106 ms                                                 | 74.3 ms: 1.42x faster                                                  |
| mako                     | 16.3 ms                                                | 11.5 ms: 1.42x faster                                                  |
| pycparser                | 1.58 sec                                               | 1.11 sec: 1.42x faster                                                 |
| 2to3                     | 348 ms                                                 | 247 ms: 1.41x faster                                                   |
| pprint_pformat           | 2.10 sec                                               | 1.49 sec: 1.41x faster                                                 |
| pathlib                  | 20.5 ms                                                | 14.6 ms: 1.41x faster                                                  |
| sqlglot_normalize        | 143 ms                                                 | 102 ms: 1.40x faster                                                   |
| pprint_safe_repr         | 1.02 sec                                               | 732 ms: 1.39x faster                                                   |
| sqlalchemy_declarative   | 172 ms                                                 | 124 ms: 1.39x faster                                                   |
| genshi_xml               | 66.0 ms                                                | 47.6 ms: 1.39x faster                                                  |
| sympy_sum                | 196 ms                                                 | 142 ms: 1.38x faster                                                   |
| fannkuch                 | 532 ms                                                 | 386 ms: 1.38x faster                                                   |
| xml_etree_process        | 79.1 ms                                                | 57.5 ms: 1.38x faster                                                  |
| sympy_integrate          | 25.8 ms                                                | 18.9 ms: 1.36x faster                                                  |
| dulwich_log              | 84.3 ms                                                | 62.0 ms: 1.36x faster                                                  |
| sqlglot_optimize         | 69.2 ms                                                | 51.5 ms: 1.34x faster                                                  |
| sympy_str                | 346 ms                                                 | 258 ms: 1.34x faster                                                   |
| sympy_expand             | 566 ms                                                 | 435 ms: 1.30x faster                                                   |
| docutils                 | 3.30 sec                                               | 2.56 sec: 1.29x faster                                                 |
| bench_thread_pool        | 986 us                                                 | 826 us: 1.19x faster                                                   |
| xml_etree_generate       | 99.4 ms                                                | 84.6 ms: 1.18x faster                                                  |
| async_generators         | 444 ms                                                 | 382 ms: 1.16x faster                                                   |
| json_dumps               | 14.2 ms                                                | 12.2 ms: 1.16x faster                                                  |
| xml_etree_iterparse      | 115 ms                                                 | 99.7 ms: 1.16x faster                                                  |
| python_startup           | 14.6 ms                                                | 12.6 ms: 1.15x faster                                                  |
| regex_dna                | 227 ms                                                 | 197 ms: 1.15x faster                                                   |
| regex_effbot             | 3.63 ms                                                | 3.20 ms: 1.13x faster                                                  |
| sqlite_synth             | 3.02 us                                                | 2.67 us: 1.13x faster                                                  |
| meteor_contest           | 120 ms                                                 | 107 ms: 1.12x faster                                                   |
| regex_v8                 | 27.8 ms                                                | 25.2 ms: 1.10x faster                                                  |
| mdp                      | 2.85 sec                                               | 2.60 sec: 1.09x faster                                                 |
| xml_etree_parse          | 168 ms                                                 | 156 ms: 1.08x faster                                                   |
| json                     | 5.69 ms                                                | 5.39 ms: 1.06x faster                                                  |
| json_loads               | 31.2 us                                                | 30.2 us: 1.03x faster                                                  |
| asyncio_websockets       | 559 ms                                                 | 553 ms: 1.01x faster                                                   |
| telco                    | 7.27 ms                                                | 7.21 ms: 1.01x faster                                                  |
| pidigits                 | 191 ms                                                 | 212 ms: 1.11x slower                                                   |
| python_startup_no_site   | 5.93 ms                                                | 6.96 ms: 1.17x slower                                                  |
| gc_traversal             | 3.62 ms                                                | 4.91 ms: 1.36x slower                                                  |
| create_gc_cycles         | 1.62 ms                                                | 2.52 ms: 1.56x slower                                                  |
| bench_mp_pool            | 24.0 ms                                                | 79.7 ms: 3.32x slower                                                  |
| Geometric mean           | (ref)                                                  | 1.48x faster                                                           |

Benchmark hidden because not significant (1): coverage
Ignored benchmarks (16) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (11) of results/bm-20250208-3.14.0a4+-29f8a67-CLANG/bm-20250208-linux-x86_64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.503x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.39x
- 95% likely to have a speedup of 1.38x
- 99% likely to have a speedup of 1.37x

# Memory
- memory change: 1.27x