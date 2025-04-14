# Results vs. 3.10.4

- fork: python
- ref: 94cd2e0ddeff83dee325
- machine: linux-x86_64
- commit hash: 94cd2e0
- commit date: 2025-02-10
- overall geometric mean: 1.442x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.31x faster
- Memory change: 1.28x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250210-linux-x86_64-python-94cd2e0ddeff83dee325-3.14.0a4+-94cd2e0 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 258 ms: 1.35x faster                                                   |
| docutils       | 3.30 sec                                               | 2.69 sec: 1.22x faster                                                 |
| html5lib       | 88.9 ms                                                | 62.2 ms: 1.43x faster                                                  |
| Geometric mean | (ref)                                                  | 1.33x faster                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250210-linux-x86_64-python-94cd2e0ddeff83dee325-3.14.0a4+-94cd2e0 |
|-------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_io           | 1.77 sec                                               | 627 ms: 2.82x faster                                                   |
| async_tree_none         | 728 ms                                                 | 269 ms: 2.71x faster                                                   |
| async_tree_memoization  | 870 ms                                                 | 328 ms: 2.65x faster                                                   |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 494 ms: 2.06x faster                                                   |
| Geometric mean          | (ref)                                                  | 2.54x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250210-linux-x86_64-python-94cd2e0ddeff83dee325-3.14.0a4+-94cd2e0 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| float          | 117 ms                                                 | 69.9 ms: 1.67x faster                                                  |
| nbody          | 154 ms                                                 | 96.6 ms: 1.59x faster                                                  |
| pidigits       | 191 ms                                                 | 186 ms: 1.03x faster                                                   |
| Geometric mean | (ref)                                                  | 1.40x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250210-linux-x86_64-python-94cd2e0ddeff83dee325-3.14.0a4+-94cd2e0 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 127 ms: 1.48x faster                                                   |
| regex_effbot   | 3.63 ms                                                | 3.09 ms: 1.17x faster                                                  |
| regex_v8       | 27.8 ms                                                | 24.1 ms: 1.15x faster                                                  |
| regex_dna      | 227 ms                                                 | 209 ms: 1.08x faster                                                   |
| Geometric mean | (ref)                                                  | 1.21x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250210-linux-x86_64-python-94cd2e0ddeff83dee325-3.14.0a4+-94cd2e0 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| tomli_loads          | 3.14 sec                                               | 1.85 sec: 1.70x faster                                                 |
| unpickle_pure_python | 331 us                                                 | 201 us: 1.64x faster                                                   |
| pickle_pure_python   | 484 us                                                 | 318 us: 1.52x faster                                                   |
| xml_etree_process    | 79.1 ms                                                | 56.1 ms: 1.41x faster                                                  |
| xml_etree_generate   | 99.4 ms                                                | 79.1 ms: 1.26x faster                                                  |
| xml_etree_parse      | 168 ms                                                 | 137 ms: 1.23x faster                                                   |
| xml_etree_iterparse  | 115 ms                                                 | 95.0 ms: 1.22x faster                                                  |
| json_dumps           | 14.2 ms                                                | 11.8 ms: 1.20x faster                                                  |
| json_loads           | 31.2 us                                                | 28.8 us: 1.08x faster                                                  |
| Geometric mean       | (ref)                                                  | 1.35x faster                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250210-linux-x86_64-python-94cd2e0ddeff83dee325-3.14.0a4+-94cd2e0 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 12.8 ms: 1.14x faster                                                  |
| python_startup_no_site | 5.93 ms                                                | 7.06 ms: 1.19x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.02x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250210-linux-x86_64-python-94cd2e0ddeff83dee325-3.14.0a4+-94cd2e0 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| mako            | 16.3 ms                                                | 9.83 ms: 1.66x faster                                                  |
| django_template | 48.2 ms                                                | 32.1 ms: 1.50x faster                                                  |
| genshi_text     | 31.8 ms                                                | 22.3 ms: 1.43x faster                                                  |
| genshi_xml      | 66.0 ms                                                | 49.6 ms: 1.33x faster                                                  |
| Geometric mean  | (ref)                                                  | 1.48x faster                                                           |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250210-linux-x86_64-python-94cd2e0ddeff83dee325-3.14.0a4+-94cd2e0 |
|--------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 163 us: 3.33x faster                                                   |
| generators               | 80.1 ms                                                | 28.3 ms: 2.83x faster                                                  |
| async_tree_io            | 1.77 sec                                               | 627 ms: 2.82x faster                                                   |
| async_tree_none          | 728 ms                                                 | 269 ms: 2.71x faster                                                   |
| async_tree_memoization   | 870 ms                                                 | 328 ms: 2.65x faster                                                   |
| deltablue                | 7.91 ms                                                | 3.44 ms: 2.30x faster                                                  |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 494 ms: 2.06x faster                                                   |
| pylint                   | 551 ms                                                 | 279 ms: 1.97x faster                                                   |
| chaos                    | 115 ms                                                 | 58.8 ms: 1.96x faster                                                  |
| deepcopy_memo            | 58.5 us                                                | 30.7 us: 1.91x faster                                                  |
| scimark_sor              | 220 ms                                                 | 119 ms: 1.84x faster                                                   |
| crypto_pyaes             | 128 ms                                                 | 69.6 ms: 1.84x faster                                                  |
| richards_super           | 94.7 ms                                                | 51.6 ms: 1.84x faster                                                  |
| deepcopy                 | 479 us                                                 | 261 us: 1.84x faster                                                   |
| go                       | 240 ms                                                 | 131 ms: 1.83x faster                                                   |
| raytrace                 | 507 ms                                                 | 281 ms: 1.81x faster                                                   |
| scimark_monte_carlo      | 118 ms                                                 | 66.4 ms: 1.78x faster                                                  |
| richards                 | 79.3 ms                                                | 45.5 ms: 1.74x faster                                                  |
| spectral_norm            | 170 ms                                                 | 98.5 ms: 1.73x faster                                                  |
| logging_silent           | 190 ns                                                 | 110 ns: 1.72x faster                                                   |
| sqlglot_parse            | 2.17 ms                                                | 1.27 ms: 1.71x faster                                                  |
| tomli_loads              | 3.14 sec                                               | 1.85 sec: 1.70x faster                                                 |
| float                    | 117 ms                                                 | 69.9 ms: 1.67x faster                                                  |
| comprehensions           | 28.8 us                                                | 17.2 us: 1.67x faster                                                  |
| mako                     | 16.3 ms                                                | 9.83 ms: 1.66x faster                                                  |
| unpickle_pure_python     | 331 us                                                 | 201 us: 1.64x faster                                                   |
| sqlglot_transpile        | 2.57 ms                                                | 1.59 ms: 1.62x faster                                                  |
| pyflate                  | 716 ms                                                 | 444 ms: 1.61x faster                                                   |
| nbody                    | 154 ms                                                 | 96.6 ms: 1.59x faster                                                  |
| deepcopy_reduce          | 4.17 us                                                | 2.68 us: 1.56x faster                                                  |
| scimark_lu               | 176 ms                                                 | 115 ms: 1.53x faster                                                   |
| pickle_pure_python       | 484 us                                                 | 318 us: 1.52x faster                                                   |
| coroutines               | 35.1 ms                                                | 23.0 ms: 1.52x faster                                                  |
| django_template          | 48.2 ms                                                | 32.1 ms: 1.50x faster                                                  |
| hexiom                   | 10.4 ms                                                | 6.95 ms: 1.50x faster                                                  |
| regex_compile            | 188 ms                                                 | 127 ms: 1.48x faster                                                   |
| scimark_fft              | 466 ms                                                 | 315 ms: 1.48x faster                                                   |
| logging_simple           | 8.30 us                                                | 5.63 us: 1.48x faster                                                  |
| logging_format           | 9.09 us                                                | 6.24 us: 1.46x faster                                                  |
| html5lib                 | 88.9 ms                                                | 62.2 ms: 1.43x faster                                                  |
| genshi_text              | 31.8 ms                                                | 22.3 ms: 1.43x faster                                                  |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.57 ms: 1.42x faster                                                  |
| xml_etree_process        | 79.1 ms                                                | 56.1 ms: 1.41x faster                                                  |
| thrift                   | 1.07 ms                                                | 772 us: 1.39x faster                                                   |
| sqlalchemy_imperative    | 23.3 ms                                                | 16.9 ms: 1.38x faster                                                  |
| pprint_pformat           | 2.10 sec                                               | 1.54 sec: 1.37x faster                                                 |
| pycparser                | 1.58 sec                                               | 1.16 sec: 1.36x faster                                                 |
| pprint_safe_repr         | 1.02 sec                                               | 748 ms: 1.36x faster                                                   |
| 2to3                     | 348 ms                                                 | 258 ms: 1.35x faster                                                   |
| sqlglot_normalize        | 143 ms                                                 | 107 ms: 1.34x faster                                                   |
| fannkuch                 | 532 ms                                                 | 397 ms: 1.34x faster                                                   |
| genshi_xml               | 66.0 ms                                                | 49.6 ms: 1.33x faster                                                  |
| sqlalchemy_declarative   | 172 ms                                                 | 131 ms: 1.32x faster                                                   |
| sympy_sum                | 196 ms                                                 | 151 ms: 1.30x faster                                                   |
| sqlglot_optimize         | 69.2 ms                                                | 53.7 ms: 1.29x faster                                                  |
| dulwich_log              | 84.3 ms                                                | 66.2 ms: 1.27x faster                                                  |
| sympy_integrate          | 25.8 ms                                                | 20.3 ms: 1.27x faster                                                  |
| xml_etree_generate       | 99.4 ms                                                | 79.1 ms: 1.26x faster                                                  |
| sympy_str                | 346 ms                                                 | 276 ms: 1.25x faster                                                   |
| xml_etree_parse          | 168 ms                                                 | 137 ms: 1.23x faster                                                   |
| docutils                 | 3.30 sec                                               | 2.69 sec: 1.22x faster                                                 |
| pathlib                  | 20.5 ms                                                | 16.7 ms: 1.22x faster                                                  |
| xml_etree_iterparse      | 115 ms                                                 | 95.0 ms: 1.22x faster                                                  |
| json_dumps               | 14.2 ms                                                | 11.8 ms: 1.20x faster                                                  |
| sympy_expand             | 566 ms                                                 | 472 ms: 1.20x faster                                                   |
| nqueens                  | 106 ms                                                 | 89.4 ms: 1.18x faster                                                  |
| regex_effbot             | 3.63 ms                                                | 3.09 ms: 1.17x faster                                                  |
| regex_v8                 | 27.8 ms                                                | 24.1 ms: 1.15x faster                                                  |
| python_startup           | 14.6 ms                                                | 12.8 ms: 1.14x faster                                                  |
| mdp                      | 2.85 sec                                               | 2.55 sec: 1.12x faster                                                 |
| bench_thread_pool        | 986 us                                                 | 888 us: 1.11x faster                                                   |
| sqlite_synth             | 3.02 us                                                | 2.73 us: 1.11x faster                                                  |
| meteor_contest           | 120 ms                                                 | 109 ms: 1.10x faster                                                   |
| json                     | 5.69 ms                                                | 5.18 ms: 1.10x faster                                                  |
| regex_dna                | 227 ms                                                 | 209 ms: 1.08x faster                                                   |
| json_loads               | 31.2 us                                                | 28.8 us: 1.08x faster                                                  |
| async_generators         | 444 ms                                                 | 411 ms: 1.08x faster                                                   |
| pidigits                 | 191 ms                                                 | 186 ms: 1.03x faster                                                   |
| asyncio_websockets       | 559 ms                                                 | 552 ms: 1.01x faster                                                   |
| telco                    | 7.27 ms                                                | 7.63 ms: 1.05x slower                                                  |
| coverage                 | 79.4 ms                                                | 90.2 ms: 1.13x slower                                                  |
| python_startup_no_site   | 5.93 ms                                                | 7.06 ms: 1.19x slower                                                  |
| gc_traversal             | 3.62 ms                                                | 4.63 ms: 1.28x slower                                                  |
| create_gc_cycles         | 1.62 ms                                                | 2.45 ms: 1.51x slower                                                  |
| bench_mp_pool            | 24.0 ms                                                | 81.2 ms: 3.38x slower                                                  |
| Geometric mean           | (ref)                                                  | 1.41x faster                                                           |
Ignored benchmarks (16) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (11) of results/bm-20250210-3.14.0a4+-94cd2e0-JIT/bm-20250210-linux-x86_64-python-94cd2e0ddeff83dee325-3.14.0a4+-94cd2e0.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.442x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.34x
- 95% likely to have a speedup of 1.33x
- 99% likely to have a speedup of 1.31x

# Memory
- memory change: 1.28x