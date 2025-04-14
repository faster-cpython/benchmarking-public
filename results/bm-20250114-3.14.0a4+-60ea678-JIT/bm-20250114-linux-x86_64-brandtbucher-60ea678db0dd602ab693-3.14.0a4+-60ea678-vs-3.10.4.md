# Results vs. 3.10.4

- fork: brandtbucher
- ref: 60ea678db0dd602ab693
- machine: linux-x86_64
- commit hash: 60ea678
- commit date: 2025-01-14
- overall geometric mean: 1.425x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.28x faster
- Memory change: 1.28x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250114-linux-x86_64-brandtbucher-60ea678db0dd602ab693-3.14.0a4+-60ea678 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 261 ms: 1.34x faster                                                         |
| docutils       | 3.30 sec                                               | 2.70 sec: 1.22x faster                                                       |
| html5lib       | 88.9 ms                                                | 63.8 ms: 1.39x faster                                                        |
| Geometric mean | (ref)                                                  | 1.31x faster                                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250114-linux-x86_64-brandtbucher-60ea678db0dd602ab693-3.14.0a4+-60ea678 |
|-------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_io           | 1.77 sec                                               | 617 ms: 2.87x faster                                                         |
| async_tree_none         | 728 ms                                                 | 267 ms: 2.73x faster                                                         |
| async_tree_memoization  | 870 ms                                                 | 333 ms: 2.62x faster                                                         |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 492 ms: 2.07x faster                                                         |
| Geometric mean          | (ref)                                                  | 2.55x faster                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250114-linux-x86_64-brandtbucher-60ea678db0dd602ab693-3.14.0a4+-60ea678 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| float          | 117 ms                                                 | 70.2 ms: 1.67x faster                                                        |
| nbody          | 154 ms                                                 | 93.8 ms: 1.64x faster                                                        |
| pidigits       | 191 ms                                                 | 186 ms: 1.03x faster                                                         |
| Geometric mean | (ref)                                                  | 1.41x faster                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250114-linux-x86_64-brandtbucher-60ea678db0dd602ab693-3.14.0a4+-60ea678 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 128 ms: 1.47x faster                                                         |
| regex_effbot   | 3.63 ms                                                | 3.00 ms: 1.21x faster                                                        |
| regex_v8       | 27.8 ms                                                | 23.9 ms: 1.16x faster                                                        |
| regex_dna      | 227 ms                                                 | 202 ms: 1.12x faster                                                         |
| Geometric mean | (ref)                                                  | 1.23x faster                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250114-linux-x86_64-brandtbucher-60ea678db0dd602ab693-3.14.0a4+-60ea678 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| tomli_loads          | 3.14 sec                                               | 1.83 sec: 1.72x faster                                                       |
| unpickle_pure_python | 331 us                                                 | 194 us: 1.70x faster                                                         |
| pickle_pure_python   | 484 us                                                 | 319 us: 1.52x faster                                                         |
| xml_etree_process    | 79.1 ms                                                | 54.7 ms: 1.45x faster                                                        |
| xml_etree_generate   | 99.4 ms                                                | 78.1 ms: 1.27x faster                                                        |
| xml_etree_parse      | 168 ms                                                 | 137 ms: 1.23x faster                                                         |
| xml_etree_iterparse  | 115 ms                                                 | 94.5 ms: 1.22x faster                                                        |
| json_dumps           | 14.2 ms                                                | 11.6 ms: 1.22x faster                                                        |
| json_loads           | 31.2 us                                                | 29.4 us: 1.06x faster                                                        |
| Geometric mean       | (ref)                                                  | 1.36x faster                                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250114-linux-x86_64-brandtbucher-60ea678db0dd602ab693-3.14.0a4+-60ea678 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 12.8 ms: 1.14x faster                                                        |
| python_startup_no_site | 5.93 ms                                                | 7.06 ms: 1.19x slower                                                        |
| Geometric mean         | (ref)                                                  | 1.02x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250114-linux-x86_64-brandtbucher-60ea678db0dd602ab693-3.14.0a4+-60ea678 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| mako            | 16.3 ms                                                | 10.1 ms: 1.61x faster                                                        |
| django_template | 48.2 ms                                                | 33.8 ms: 1.42x faster                                                        |
| genshi_text     | 31.8 ms                                                | 24.1 ms: 1.32x faster                                                        |
| genshi_xml      | 66.0 ms                                                | 60.5 ms: 1.09x faster                                                        |
| Geometric mean  | (ref)                                                  | 1.35x faster                                                                 |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250114-linux-x86_64-brandtbucher-60ea678db0dd602ab693-3.14.0a4+-60ea678 |
|--------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 166 us: 3.27x faster                                                         |
| async_tree_io            | 1.77 sec                                               | 617 ms: 2.87x faster                                                         |
| async_tree_none          | 728 ms                                                 | 267 ms: 2.73x faster                                                         |
| async_tree_memoization   | 870 ms                                                 | 333 ms: 2.62x faster                                                         |
| deltablue                | 7.91 ms                                                | 3.27 ms: 2.42x faster                                                        |
| generators               | 80.1 ms                                                | 37.5 ms: 2.14x faster                                                        |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 492 ms: 2.07x faster                                                         |
| deepcopy_memo            | 58.5 us                                                | 29.9 us: 1.95x faster                                                        |
| pylint                   | 551 ms                                                 | 287 ms: 1.92x faster                                                         |
| scimark_monte_carlo      | 118 ms                                                 | 63.0 ms: 1.87x faster                                                        |
| scimark_sor              | 220 ms                                                 | 117 ms: 1.87x faster                                                         |
| richards_super           | 94.7 ms                                                | 50.9 ms: 1.86x faster                                                        |
| chaos                    | 115 ms                                                 | 62.7 ms: 1.84x faster                                                        |
| richards                 | 79.3 ms                                                | 44.2 ms: 1.79x faster                                                        |
| deepcopy                 | 479 us                                                 | 268 us: 1.79x faster                                                         |
| go                       | 240 ms                                                 | 135 ms: 1.77x faster                                                         |
| crypto_pyaes             | 128 ms                                                 | 72.2 ms: 1.77x faster                                                        |
| raytrace                 | 507 ms                                                 | 291 ms: 1.74x faster                                                         |
| logging_silent           | 190 ns                                                 | 111 ns: 1.72x faster                                                         |
| tomli_loads              | 3.14 sec                                               | 1.83 sec: 1.72x faster                                                       |
| sqlglot_parse            | 2.17 ms                                                | 1.27 ms: 1.70x faster                                                        |
| unpickle_pure_python     | 331 us                                                 | 194 us: 1.70x faster                                                         |
| comprehensions           | 28.8 us                                                | 17.2 us: 1.67x faster                                                        |
| float                    | 117 ms                                                 | 70.2 ms: 1.67x faster                                                        |
| nbody                    | 154 ms                                                 | 93.8 ms: 1.64x faster                                                        |
| sqlglot_transpile        | 2.57 ms                                                | 1.59 ms: 1.62x faster                                                        |
| mako                     | 16.3 ms                                                | 10.1 ms: 1.61x faster                                                        |
| pyflate                  | 716 ms                                                 | 449 ms: 1.60x faster                                                         |
| scimark_lu               | 176 ms                                                 | 114 ms: 1.55x faster                                                         |
| deepcopy_reduce          | 4.17 us                                                | 2.72 us: 1.53x faster                                                        |
| pickle_pure_python       | 484 us                                                 | 319 us: 1.52x faster                                                         |
| coroutines               | 35.1 ms                                                | 23.8 ms: 1.47x faster                                                        |
| regex_compile            | 188 ms                                                 | 128 ms: 1.47x faster                                                         |
| hexiom                   | 10.4 ms                                                | 7.18 ms: 1.45x faster                                                        |
| xml_etree_process        | 79.1 ms                                                | 54.7 ms: 1.45x faster                                                        |
| logging_simple           | 8.30 us                                                | 5.77 us: 1.44x faster                                                        |
| logging_format           | 9.09 us                                                | 6.35 us: 1.43x faster                                                        |
| django_template          | 48.2 ms                                                | 33.8 ms: 1.42x faster                                                        |
| scimark_fft              | 466 ms                                                 | 331 ms: 1.41x faster                                                         |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.60 ms: 1.41x faster                                                        |
| pprint_pformat           | 2.10 sec                                               | 1.50 sec: 1.40x faster                                                       |
| spectral_norm            | 170 ms                                                 | 121 ms: 1.40x faster                                                         |
| pprint_safe_repr         | 1.02 sec                                               | 728 ms: 1.40x faster                                                         |
| html5lib                 | 88.9 ms                                                | 63.8 ms: 1.39x faster                                                        |
| thrift                   | 1.07 ms                                                | 771 us: 1.39x faster                                                         |
| sqlalchemy_imperative    | 23.3 ms                                                | 16.9 ms: 1.38x faster                                                        |
| fannkuch                 | 532 ms                                                 | 389 ms: 1.37x faster                                                         |
| 2to3                     | 348 ms                                                 | 261 ms: 1.34x faster                                                         |
| pycparser                | 1.58 sec                                               | 1.18 sec: 1.34x faster                                                       |
| sqlglot_normalize        | 143 ms                                                 | 108 ms: 1.32x faster                                                         |
| genshi_text              | 31.8 ms                                                | 24.1 ms: 1.32x faster                                                        |
| sqlalchemy_declarative   | 172 ms                                                 | 131 ms: 1.31x faster                                                         |
| xml_etree_generate       | 99.4 ms                                                | 78.1 ms: 1.27x faster                                                        |
| sqlglot_optimize         | 69.2 ms                                                | 54.6 ms: 1.27x faster                                                        |
| sympy_sum                | 196 ms                                                 | 156 ms: 1.26x faster                                                         |
| dulwich_log              | 84.3 ms                                                | 67.4 ms: 1.25x faster                                                        |
| sympy_integrate          | 25.8 ms                                                | 20.6 ms: 1.25x faster                                                        |
| pathlib                  | 20.5 ms                                                | 16.5 ms: 1.24x faster                                                        |
| sympy_str                | 346 ms                                                 | 280 ms: 1.23x faster                                                         |
| xml_etree_parse          | 168 ms                                                 | 137 ms: 1.23x faster                                                         |
| xml_etree_iterparse      | 115 ms                                                 | 94.5 ms: 1.22x faster                                                        |
| docutils                 | 3.30 sec                                               | 2.70 sec: 1.22x faster                                                       |
| json_dumps               | 14.2 ms                                                | 11.6 ms: 1.22x faster                                                        |
| regex_effbot             | 3.63 ms                                                | 3.00 ms: 1.21x faster                                                        |
| sympy_expand             | 566 ms                                                 | 476 ms: 1.19x faster                                                         |
| nqueens                  | 106 ms                                                 | 89.8 ms: 1.18x faster                                                        |
| regex_v8                 | 27.8 ms                                                | 23.9 ms: 1.16x faster                                                        |
| python_startup           | 14.6 ms                                                | 12.8 ms: 1.14x faster                                                        |
| regex_dna                | 227 ms                                                 | 202 ms: 1.12x faster                                                         |
| mdp                      | 2.85 sec                                               | 2.56 sec: 1.11x faster                                                       |
| sqlite_synth             | 3.02 us                                                | 2.74 us: 1.11x faster                                                        |
| bench_thread_pool        | 986 us                                                 | 895 us: 1.10x faster                                                         |
| meteor_contest           | 120 ms                                                 | 109 ms: 1.10x faster                                                         |
| genshi_xml               | 66.0 ms                                                | 60.5 ms: 1.09x faster                                                        |
| json                     | 5.69 ms                                                | 5.21 ms: 1.09x faster                                                        |
| async_generators         | 444 ms                                                 | 408 ms: 1.09x faster                                                         |
| json_loads               | 31.2 us                                                | 29.4 us: 1.06x faster                                                        |
| pidigits                 | 191 ms                                                 | 186 ms: 1.03x faster                                                         |
| asyncio_websockets       | 559 ms                                                 | 552 ms: 1.01x faster                                                         |
| telco                    | 7.27 ms                                                | 7.55 ms: 1.04x slower                                                        |
| coverage                 | 79.4 ms                                                | 90.2 ms: 1.14x slower                                                        |
| python_startup_no_site   | 5.93 ms                                                | 7.06 ms: 1.19x slower                                                        |
| gc_traversal             | 3.62 ms                                                | 4.84 ms: 1.34x slower                                                        |
| create_gc_cycles         | 1.62 ms                                                | 2.44 ms: 1.51x slower                                                        |
| bench_mp_pool            | 24.0 ms                                                | 81.2 ms: 3.38x slower                                                        |
| Geometric mean           | (ref)                                                  | 1.40x faster                                                                 |
Ignored benchmarks (16) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (11) of results/bm-20250114-3.14.0a4+-60ea678-JIT/bm-20250114-linux-x86_64-brandtbucher-60ea678db0dd602ab693-3.14.0a4+-60ea678.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.425x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.33x
- 95% likely to have a speedup of 1.32x
- 99% likely to have a speedup of 1.28x

# Memory
- memory change: 1.28x