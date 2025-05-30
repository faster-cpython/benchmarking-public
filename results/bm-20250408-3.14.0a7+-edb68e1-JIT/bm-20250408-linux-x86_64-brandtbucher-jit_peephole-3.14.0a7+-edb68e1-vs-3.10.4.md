# Results vs. 3.10.4

- fork: brandtbucher
- ref: jit_peephole
- machine: linux-x86_64
- commit hash: edb68e1
- commit date: 2025-04-08
- overall geometric mean: 1.476x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.33x faster
- Memory change: 1.29x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250408-linux-x86_64-brandtbucher-jit_peephole-3.14.0a7+-edb68e1 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 254 ms: 1.37x faster                                                 |
| docutils       | 3.30 sec                                               | 2.66 sec: 1.24x faster                                               |
| html5lib       | 88.9 ms                                                | 60.9 ms: 1.46x faster                                                |
| Geometric mean | (ref)                                                  | 1.35x faster                                                         |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250408-linux-x86_64-brandtbucher-jit_peephole-3.14.0a7+-edb68e1 |
|-------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| async_tree_io           | 1.77 sec                                               | 613 ms: 2.89x faster                                                 |
| async_tree_none         | 728 ms                                                 | 260 ms: 2.80x faster                                                 |
| async_tree_memoization  | 870 ms                                                 | 313 ms: 2.78x faster                                                 |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 495 ms: 2.05x faster                                                 |
| Geometric mean          | (ref)                                                  | 2.61x faster                                                         |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250408-linux-x86_64-brandtbucher-jit_peephole-3.14.0a7+-edb68e1 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 88.4 ms: 1.74x faster                                                |
| float          | 117 ms                                                 | 68.8 ms: 1.70x faster                                                |
| pidigits       | 191 ms                                                 | 186 ms: 1.03x faster                                                 |
| Geometric mean | (ref)                                                  | 1.45x faster                                                         |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250408-linux-x86_64-brandtbucher-jit_peephole-3.14.0a7+-edb68e1 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 125 ms: 1.51x faster                                                 |
| regex_v8       | 27.8 ms                                                | 21.9 ms: 1.27x faster                                                |
| regex_effbot   | 3.63 ms                                                | 3.22 ms: 1.13x faster                                                |
| regex_dna      | 227 ms                                                 | 207 ms: 1.09x faster                                                 |
| Geometric mean | (ref)                                                  | 1.24x faster                                                         |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250408-linux-x86_64-brandtbucher-jit_peephole-3.14.0a7+-edb68e1 |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| tomli_loads          | 3.14 sec                                               | 1.83 sec: 1.72x faster                                               |
| unpickle_pure_python | 331 us                                                 | 208 us: 1.59x faster                                                 |
| pickle_pure_python   | 484 us                                                 | 319 us: 1.52x faster                                                 |
| xml_etree_process    | 79.1 ms                                                | 56.6 ms: 1.40x faster                                                |
| json_dumps           | 14.2 ms                                                | 11.5 ms: 1.24x faster                                                |
| xml_etree_generate   | 99.4 ms                                                | 81.0 ms: 1.23x faster                                                |
| xml_etree_parse      | 168 ms                                                 | 139 ms: 1.21x faster                                                 |
| xml_etree_iterparse  | 115 ms                                                 | 97.1 ms: 1.19x faster                                                |
| json_loads           | 31.2 us                                                | 29.4 us: 1.06x faster                                                |
| Geometric mean       | (ref)                                                  | 1.33x faster                                                         |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250408-linux-x86_64-brandtbucher-jit_peephole-3.14.0a7+-edb68e1 |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 13.1 ms: 1.11x faster                                                |
| python_startup_no_site | 5.93 ms                                                | 8.18 ms: 1.38x slower                                                |
| Geometric mean         | (ref)                                                  | 1.11x slower                                                         |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250408-linux-x86_64-brandtbucher-jit_peephole-3.14.0a7+-edb68e1 |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| genshi_text     | 31.8 ms                                                | 20.7 ms: 1.54x faster                                                |
| mako            | 16.3 ms                                                | 10.8 ms: 1.51x faster                                                |
| django_template | 48.2 ms                                                | 32.2 ms: 1.50x faster                                                |
| genshi_xml      | 66.0 ms                                                | 49.0 ms: 1.35x faster                                                |
| Geometric mean  | (ref)                                                  | 1.47x faster                                                         |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250408-linux-x86_64-brandtbucher-jit_peephole-3.14.0a7+-edb68e1 |
|--------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 167 us: 3.26x faster                                                 |
| async_tree_io            | 1.77 sec                                               | 613 ms: 2.89x faster                                                 |
| async_tree_none          | 728 ms                                                 | 260 ms: 2.80x faster                                                 |
| async_tree_memoization   | 870 ms                                                 | 313 ms: 2.78x faster                                                 |
| generators               | 80.1 ms                                                | 29.0 ms: 2.76x faster                                                |
| deltablue                | 7.91 ms                                                | 3.04 ms: 2.60x faster                                                |
| mdp                      | 2.85 sec                                               | 1.22 sec: 2.33x faster                                               |
| richards_super           | 94.7 ms                                                | 42.0 ms: 2.26x faster                                                |
| richards                 | 79.3 ms                                                | 35.8 ms: 2.22x faster                                                |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 495 ms: 2.05x faster                                                 |
| chaos                    | 115 ms                                                 | 56.4 ms: 2.05x faster                                                |
| deepcopy_memo            | 58.5 us                                                | 28.7 us: 2.04x faster                                                |
| go                       | 240 ms                                                 | 120 ms: 2.01x faster                                                 |
| pylint                   | 551 ms                                                 | 279 ms: 1.98x faster                                                 |
| raytrace                 | 507 ms                                                 | 260 ms: 1.95x faster                                                 |
| logging_silent           | 190 ns                                                 | 98.2 ns: 1.93x faster                                                |
| scimark_sor              | 220 ms                                                 | 115 ms: 1.91x faster                                                 |
| deepcopy                 | 479 us                                                 | 251 us: 1.91x faster                                                 |
| scimark_monte_carlo      | 118 ms                                                 | 66.1 ms: 1.79x faster                                                |
| nbody                    | 154 ms                                                 | 88.4 ms: 1.74x faster                                                |
| crypto_pyaes             | 128 ms                                                 | 74.1 ms: 1.72x faster                                                |
| tomli_loads              | 3.14 sec                                               | 1.83 sec: 1.72x faster                                               |
| spectral_norm            | 170 ms                                                 | 98.8 ms: 1.72x faster                                                |
| float                    | 117 ms                                                 | 68.8 ms: 1.70x faster                                                |
| pyflate                  | 716 ms                                                 | 422 ms: 1.70x faster                                                 |
| deepcopy_reduce          | 4.17 us                                                | 2.60 us: 1.60x faster                                                |
| unpickle_pure_python     | 331 us                                                 | 208 us: 1.59x faster                                                 |
| hexiom                   | 10.4 ms                                                | 6.60 ms: 1.58x faster                                                |
| comprehensions           | 28.8 us                                                | 18.5 us: 1.55x faster                                                |
| genshi_text              | 31.8 ms                                                | 20.7 ms: 1.54x faster                                                |
| scimark_fft              | 466 ms                                                 | 303 ms: 1.54x faster                                                 |
| pickle_pure_python       | 484 us                                                 | 319 us: 1.52x faster                                                 |
| scimark_lu               | 176 ms                                                 | 116 ms: 1.52x faster                                                 |
| mako                     | 16.3 ms                                                | 10.8 ms: 1.51x faster                                                |
| regex_compile            | 188 ms                                                 | 125 ms: 1.51x faster                                                 |
| django_template          | 48.2 ms                                                | 32.2 ms: 1.50x faster                                                |
| coroutines               | 35.1 ms                                                | 23.7 ms: 1.48x faster                                                |
| logging_simple           | 8.30 us                                                | 5.64 us: 1.47x faster                                                |
| html5lib                 | 88.9 ms                                                | 60.9 ms: 1.46x faster                                                |
| logging_format           | 9.09 us                                                | 6.23 us: 1.46x faster                                                |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.51 ms: 1.44x faster                                                |
| xml_etree_process        | 79.1 ms                                                | 56.6 ms: 1.40x faster                                                |
| pprint_safe_repr         | 1.02 sec                                               | 731 ms: 1.39x faster                                                 |
| dulwich_log              | 84.3 ms                                                | 60.7 ms: 1.39x faster                                                |
| pprint_pformat           | 2.10 sec                                               | 1.52 sec: 1.38x faster                                               |
| 2to3                     | 348 ms                                                 | 254 ms: 1.37x faster                                                 |
| sqlalchemy_imperative    | 23.3 ms                                                | 17.1 ms: 1.36x faster                                                |
| genshi_xml               | 66.0 ms                                                | 49.0 ms: 1.35x faster                                                |
| pycparser                | 1.58 sec                                               | 1.17 sec: 1.34x faster                                               |
| sympy_integrate          | 25.8 ms                                                | 19.4 ms: 1.33x faster                                                |
| sympy_sum                | 196 ms                                                 | 149 ms: 1.32x faster                                                 |
| nqueens                  | 106 ms                                                 | 81.5 ms: 1.30x faster                                                |
| sqlalchemy_declarative   | 172 ms                                                 | 133 ms: 1.30x faster                                                 |
| fannkuch                 | 532 ms                                                 | 411 ms: 1.29x faster                                                 |
| sympy_str                | 346 ms                                                 | 268 ms: 1.29x faster                                                 |
| regex_v8                 | 27.8 ms                                                | 21.9 ms: 1.27x faster                                                |
| docutils                 | 3.30 sec                                               | 2.66 sec: 1.24x faster                                               |
| json_dumps               | 14.2 ms                                                | 11.5 ms: 1.24x faster                                                |
| xml_etree_generate       | 99.4 ms                                                | 81.0 ms: 1.23x faster                                                |
| sympy_expand             | 566 ms                                                 | 466 ms: 1.21x faster                                                 |
| pathlib                  | 20.5 ms                                                | 16.9 ms: 1.21x faster                                                |
| xml_etree_parse          | 168 ms                                                 | 139 ms: 1.21x faster                                                 |
| xml_etree_iterparse      | 115 ms                                                 | 97.1 ms: 1.19x faster                                                |
| regex_effbot             | 3.63 ms                                                | 3.22 ms: 1.13x faster                                                |
| python_startup           | 14.6 ms                                                | 13.1 ms: 1.11x faster                                                |
| sqlite_synth             | 3.02 us                                                | 2.73 us: 1.11x faster                                                |
| bench_thread_pool        | 986 us                                                 | 892 us: 1.11x faster                                                 |
| meteor_contest           | 120 ms                                                 | 109 ms: 1.09x faster                                                 |
| regex_dna                | 227 ms                                                 | 207 ms: 1.09x faster                                                 |
| json                     | 5.69 ms                                                | 5.29 ms: 1.08x faster                                                |
| json_loads               | 31.2 us                                                | 29.4 us: 1.06x faster                                                |
| async_generators         | 444 ms                                                 | 418 ms: 1.06x faster                                                 |
| pidigits                 | 191 ms                                                 | 186 ms: 1.03x faster                                                 |
| asyncio_websockets       | 559 ms                                                 | 553 ms: 1.01x faster                                                 |
| telco                    | 7.27 ms                                                | 7.68 ms: 1.06x slower                                                |
| coverage                 | 79.4 ms                                                | 85.1 ms: 1.07x slower                                                |
| python_startup_no_site   | 5.93 ms                                                | 8.18 ms: 1.38x slower                                                |
| gc_traversal             | 3.62 ms                                                | 5.05 ms: 1.39x slower                                                |
| create_gc_cycles         | 1.62 ms                                                | 2.46 ms: 1.52x slower                                                |
| bench_mp_pool            | 24.0 ms                                                | 82.0 ms: 3.41x slower                                                |
| Geometric mean           | (ref)                                                  | 1.45x faster                                                         |
Ignored benchmarks (21) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (15) of results/bm-20250408-3.14.0a7+-edb68e1-JIT/bm-20250408-linux-x86_64-brandtbucher-jit_peephole-3.14.0a7+-edb68e1.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.476x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.38x
- 95% likely to have a speedup of 1.36x
- 99% likely to have a speedup of 1.33x

# Memory
- memory change: 1.29x