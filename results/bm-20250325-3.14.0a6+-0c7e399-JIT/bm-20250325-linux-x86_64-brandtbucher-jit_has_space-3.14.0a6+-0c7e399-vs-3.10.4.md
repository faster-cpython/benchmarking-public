# Results vs. 3.10.4

- fork: brandtbucher
- ref: jit_has_space
- machine: linux-x86_64
- commit hash: 0c7e399
- commit date: 2025-03-25
- overall geometric mean: 1.439x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.29x faster
- Memory change: 1.29x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250325-linux-x86_64-brandtbucher-jit_has_space-3.14.0a6+-0c7e399 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 264 ms: 1.32x faster                                                  |
| docutils       | 3.30 sec                                               | 2.68 sec: 1.23x faster                                                |
| html5lib       | 88.9 ms                                                | 63.2 ms: 1.41x faster                                                 |
| Geometric mean | (ref)                                                  | 1.32x faster                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250325-linux-x86_64-brandtbucher-jit_has_space-3.14.0a6+-0c7e399 |
|-------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_io           | 1.77 sec                                               | 626 ms: 2.82x faster                                                  |
| async_tree_memoization  | 870 ms                                                 | 317 ms: 2.74x faster                                                  |
| async_tree_none         | 728 ms                                                 | 266 ms: 2.74x faster                                                  |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 499 ms: 2.04x faster                                                  |
| Geometric mean          | (ref)                                                  | 2.56x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250325-linux-x86_64-brandtbucher-jit_has_space-3.14.0a6+-0c7e399 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 117 ms                                                 | 65.3 ms: 1.79x faster                                                 |
| nbody          | 154 ms                                                 | 87.5 ms: 1.75x faster                                                 |
| pidigits       | 191 ms                                                 | 186 ms: 1.03x faster                                                  |
| Geometric mean | (ref)                                                  | 1.48x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250325-linux-x86_64-brandtbucher-jit_has_space-3.14.0a6+-0c7e399 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 128 ms: 1.47x faster                                                  |
| regex_v8       | 27.8 ms                                                | 22.7 ms: 1.23x faster                                                 |
| regex_effbot   | 3.63 ms                                                | 3.14 ms: 1.16x faster                                                 |
| regex_dna      | 227 ms                                                 | 213 ms: 1.07x faster                                                  |
| Geometric mean | (ref)                                                  | 1.22x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250325-linux-x86_64-brandtbucher-jit_has_space-3.14.0a6+-0c7e399 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| tomli_loads          | 3.14 sec                                               | 1.87 sec: 1.68x faster                                                |
| unpickle_pure_python | 331 us                                                 | 214 us: 1.54x faster                                                  |
| pickle_pure_python   | 484 us                                                 | 322 us: 1.50x faster                                                  |
| xml_etree_process    | 79.1 ms                                                | 56.9 ms: 1.39x faster                                                 |
| xml_etree_generate   | 99.4 ms                                                | 80.7 ms: 1.23x faster                                                 |
| json_dumps           | 14.2 ms                                                | 11.6 ms: 1.23x faster                                                 |
| xml_etree_parse      | 168 ms                                                 | 140 ms: 1.20x faster                                                  |
| xml_etree_iterparse  | 115 ms                                                 | 98.4 ms: 1.17x faster                                                 |
| json_loads           | 31.2 us                                                | 29.9 us: 1.04x faster                                                 |
| Geometric mean       | (ref)                                                  | 1.32x faster                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250325-linux-x86_64-brandtbucher-jit_has_space-3.14.0a6+-0c7e399 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 13.1 ms: 1.11x faster                                                 |
| python_startup_no_site | 5.93 ms                                                | 8.18 ms: 1.38x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.11x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250325-linux-x86_64-brandtbucher-jit_has_space-3.14.0a6+-0c7e399 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| django_template | 48.2 ms                                                | 31.8 ms: 1.51x faster                                                 |
| mako            | 16.3 ms                                                | 10.9 ms: 1.50x faster                                                 |
| genshi_text     | 31.8 ms                                                | 21.4 ms: 1.48x faster                                                 |
| genshi_xml      | 66.0 ms                                                | 50.3 ms: 1.31x faster                                                 |
| Geometric mean  | (ref)                                                  | 1.45x faster                                                          |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250325-linux-x86_64-brandtbucher-jit_has_space-3.14.0a6+-0c7e399 |
|--------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 168 us: 3.24x faster                                                  |
| async_tree_io            | 1.77 sec                                               | 626 ms: 2.82x faster                                                  |
| generators               | 80.1 ms                                                | 29.2 ms: 2.75x faster                                                 |
| async_tree_memoization   | 870 ms                                                 | 317 ms: 2.74x faster                                                  |
| async_tree_none          | 728 ms                                                 | 266 ms: 2.74x faster                                                  |
| deltablue                | 7.91 ms                                                | 3.08 ms: 2.56x faster                                                 |
| richards_super           | 94.7 ms                                                | 41.3 ms: 2.29x faster                                                 |
| richards                 | 79.3 ms                                                | 36.4 ms: 2.18x faster                                                 |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 499 ms: 2.04x faster                                                  |
| deepcopy_memo            | 58.5 us                                                | 28.9 us: 2.02x faster                                                 |
| pylint                   | 551 ms                                                 | 282 ms: 1.96x faster                                                  |
| logging_silent           | 190 ns                                                 | 98.2 ns: 1.93x faster                                                 |
| chaos                    | 115 ms                                                 | 60.2 ms: 1.92x faster                                                 |
| raytrace                 | 507 ms                                                 | 271 ms: 1.87x faster                                                  |
| go                       | 240 ms                                                 | 129 ms: 1.87x faster                                                  |
| scimark_sor              | 220 ms                                                 | 119 ms: 1.85x faster                                                  |
| deepcopy                 | 479 us                                                 | 260 us: 1.85x faster                                                  |
| float                    | 117 ms                                                 | 65.3 ms: 1.79x faster                                                 |
| nbody                    | 154 ms                                                 | 87.5 ms: 1.75x faster                                                 |
| spectral_norm            | 170 ms                                                 | 97.0 ms: 1.75x faster                                                 |
| scimark_monte_carlo      | 118 ms                                                 | 68.7 ms: 1.72x faster                                                 |
| tomli_loads              | 3.14 sec                                               | 1.87 sec: 1.68x faster                                                |
| crypto_pyaes             | 128 ms                                                 | 78.2 ms: 1.63x faster                                                 |
| pyflate                  | 716 ms                                                 | 450 ms: 1.59x faster                                                  |
| unpickle_pure_python     | 331 us                                                 | 214 us: 1.54x faster                                                  |
| deepcopy_reduce          | 4.17 us                                                | 2.71 us: 1.54x faster                                                 |
| hexiom                   | 10.4 ms                                                | 6.81 ms: 1.53x faster                                                 |
| comprehensions           | 28.8 us                                                | 18.9 us: 1.52x faster                                                 |
| django_template          | 48.2 ms                                                | 31.8 ms: 1.51x faster                                                 |
| scimark_lu               | 176 ms                                                 | 117 ms: 1.50x faster                                                  |
| pickle_pure_python       | 484 us                                                 | 322 us: 1.50x faster                                                  |
| mako                     | 16.3 ms                                                | 10.9 ms: 1.50x faster                                                 |
| scimark_fft              | 466 ms                                                 | 313 ms: 1.49x faster                                                  |
| genshi_text              | 31.8 ms                                                | 21.4 ms: 1.48x faster                                                 |
| logging_simple           | 8.30 us                                                | 5.63 us: 1.47x faster                                                 |
| regex_compile            | 188 ms                                                 | 128 ms: 1.47x faster                                                  |
| logging_format           | 9.09 us                                                | 6.24 us: 1.46x faster                                                 |
| coroutines               | 35.1 ms                                                | 24.1 ms: 1.45x faster                                                 |
| html5lib                 | 88.9 ms                                                | 63.2 ms: 1.41x faster                                                 |
| xml_etree_process        | 79.1 ms                                                | 56.9 ms: 1.39x faster                                                 |
| dulwich_log              | 84.3 ms                                                | 60.8 ms: 1.39x faster                                                 |
| pycparser                | 1.58 sec                                               | 1.14 sec: 1.39x faster                                                |
| thrift                   | 1.07 ms                                                | 778 us: 1.38x faster                                                  |
| sqlalchemy_imperative    | 23.3 ms                                                | 17.1 ms: 1.37x faster                                                 |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.75 ms: 1.36x faster                                                 |
| pprint_pformat           | 2.10 sec                                               | 1.55 sec: 1.36x faster                                                |
| pprint_safe_repr         | 1.02 sec                                               | 753 ms: 1.35x faster                                                  |
| 2to3                     | 348 ms                                                 | 264 ms: 1.32x faster                                                  |
| genshi_xml               | 66.0 ms                                                | 50.3 ms: 1.31x faster                                                 |
| sqlalchemy_declarative   | 172 ms                                                 | 133 ms: 1.29x faster                                                  |
| sympy_sum                | 196 ms                                                 | 153 ms: 1.29x faster                                                  |
| sympy_integrate          | 25.8 ms                                                | 20.1 ms: 1.28x faster                                                 |
| fannkuch                 | 532 ms                                                 | 423 ms: 1.26x faster                                                  |
| sympy_str                | 346 ms                                                 | 276 ms: 1.25x faster                                                  |
| nqueens                  | 106 ms                                                 | 85.0 ms: 1.24x faster                                                 |
| xml_etree_generate       | 99.4 ms                                                | 80.7 ms: 1.23x faster                                                 |
| pathlib                  | 20.5 ms                                                | 16.6 ms: 1.23x faster                                                 |
| docutils                 | 3.30 sec                                               | 2.68 sec: 1.23x faster                                                |
| json_dumps               | 14.2 ms                                                | 11.6 ms: 1.23x faster                                                 |
| regex_v8                 | 27.8 ms                                                | 22.7 ms: 1.23x faster                                                 |
| xml_etree_parse          | 168 ms                                                 | 140 ms: 1.20x faster                                                  |
| sympy_expand             | 566 ms                                                 | 477 ms: 1.19x faster                                                  |
| xml_etree_iterparse      | 115 ms                                                 | 98.4 ms: 1.17x faster                                                 |
| regex_effbot             | 3.63 ms                                                | 3.14 ms: 1.16x faster                                                 |
| mdp                      | 2.85 sec                                               | 2.50 sec: 1.14x faster                                                |
| bench_thread_pool        | 986 us                                                 | 880 us: 1.12x faster                                                  |
| python_startup           | 14.6 ms                                                | 13.1 ms: 1.11x faster                                                 |
| sqlite_synth             | 3.02 us                                                | 2.72 us: 1.11x faster                                                 |
| meteor_contest           | 120 ms                                                 | 109 ms: 1.10x faster                                                  |
| json                     | 5.69 ms                                                | 5.32 ms: 1.07x faster                                                 |
| async_generators         | 444 ms                                                 | 415 ms: 1.07x faster                                                  |
| regex_dna                | 227 ms                                                 | 213 ms: 1.07x faster                                                  |
| json_loads               | 31.2 us                                                | 29.9 us: 1.04x faster                                                 |
| pidigits                 | 191 ms                                                 | 186 ms: 1.03x faster                                                  |
| asyncio_websockets       | 559 ms                                                 | 552 ms: 1.01x faster                                                  |
| telco                    | 7.27 ms                                                | 7.79 ms: 1.07x slower                                                 |
| coverage                 | 79.4 ms                                                | 86.7 ms: 1.09x slower                                                 |
| gc_traversal             | 3.62 ms                                                | 4.85 ms: 1.34x slower                                                 |
| python_startup_no_site   | 5.93 ms                                                | 8.18 ms: 1.38x slower                                                 |
| create_gc_cycles         | 1.62 ms                                                | 2.49 ms: 1.54x slower                                                 |
| bench_mp_pool            | 24.0 ms                                                | 82.7 ms: 3.44x slower                                                 |
| Geometric mean           | (ref)                                                  | 1.41x faster                                                          |
Ignored benchmarks (20) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (15) of results/bm-20250325-3.14.0a6+-0c7e399-JIT/bm-20250325-linux-x86_64-brandtbucher-jit_has_space-3.14.0a6+-0c7e399.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.439x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.34x
- 95% likely to have a speedup of 1.32x
- 99% likely to have a speedup of 1.29x

# Memory
- memory change: 1.29x