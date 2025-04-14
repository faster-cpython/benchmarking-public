# Results vs. 3.10.4

- fork: brandtbucher
- ref: jit_cached_consts
- machine: linux-x86_64
- commit hash: 32ebfed
- commit date: 2025-03-19
- overall geometric mean: 1.455x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.31x faster
- Memory change: 1.29x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250319-linux-x86_64-brandtbucher-jit_cached_consts-3.14.0a6+-32ebfed |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 262 ms: 1.33x faster                                                      |
| docutils       | 3.30 sec                                               | 2.69 sec: 1.23x faster                                                    |
| html5lib       | 88.9 ms                                                | 63.3 ms: 1.40x faster                                                     |
| Geometric mean | (ref)                                                  | 1.32x faster                                                              |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250319-linux-x86_64-brandtbucher-jit_cached_consts-3.14.0a6+-32ebfed |
|-------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| async_tree_io           | 1.77 sec                                               | 620 ms: 2.85x faster                                                      |
| async_tree_none         | 728 ms                                                 | 259 ms: 2.81x faster                                                      |
| async_tree_memoization  | 870 ms                                                 | 319 ms: 2.73x faster                                                      |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 496 ms: 2.05x faster                                                      |
| Geometric mean          | (ref)                                                  | 2.59x faster                                                              |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250319-linux-x86_64-brandtbucher-jit_cached_consts-3.14.0a6+-32ebfed |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| float          | 117 ms                                                 | 65.2 ms: 1.80x faster                                                     |
| nbody          | 154 ms                                                 | 86.9 ms: 1.77x faster                                                     |
| pidigits       | 191 ms                                                 | 186 ms: 1.03x faster                                                      |
| Geometric mean | (ref)                                                  | 1.48x faster                                                              |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250319-linux-x86_64-brandtbucher-jit_cached_consts-3.14.0a6+-32ebfed |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 128 ms: 1.48x faster                                                      |
| regex_v8       | 27.8 ms                                                | 23.2 ms: 1.20x faster                                                     |
| regex_effbot   | 3.63 ms                                                | 3.45 ms: 1.05x faster                                                     |
| regex_dna      | 227 ms                                                 | 221 ms: 1.03x faster                                                      |
| Geometric mean | (ref)                                                  | 1.18x faster                                                              |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250319-linux-x86_64-brandtbucher-jit_cached_consts-3.14.0a6+-32ebfed |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| tomli_loads          | 3.14 sec                                               | 1.86 sec: 1.69x faster                                                    |
| unpickle_pure_python | 331 us                                                 | 213 us: 1.55x faster                                                      |
| pickle_pure_python   | 484 us                                                 | 321 us: 1.51x faster                                                      |
| xml_etree_process    | 79.1 ms                                                | 55.5 ms: 1.43x faster                                                     |
| xml_etree_generate   | 99.4 ms                                                | 79.3 ms: 1.25x faster                                                     |
| json_dumps           | 14.2 ms                                                | 11.5 ms: 1.23x faster                                                     |
| xml_etree_parse      | 168 ms                                                 | 140 ms: 1.20x faster                                                      |
| xml_etree_iterparse  | 115 ms                                                 | 97.7 ms: 1.18x faster                                                     |
| json_loads           | 31.2 us                                                | 29.8 us: 1.05x faster                                                     |
| Geometric mean       | (ref)                                                  | 1.33x faster                                                              |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250319-linux-x86_64-brandtbucher-jit_cached_consts-3.14.0a6+-32ebfed |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 13.1 ms: 1.11x faster                                                     |
| python_startup_no_site | 5.93 ms                                                | 8.20 ms: 1.38x slower                                                     |
| Geometric mean         | (ref)                                                  | 1.12x slower                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250319-linux-x86_64-brandtbucher-jit_cached_consts-3.14.0a6+-32ebfed |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| django_template | 48.2 ms                                                | 31.6 ms: 1.53x faster                                                     |
| genshi_text     | 31.8 ms                                                | 21.0 ms: 1.51x faster                                                     |
| mako            | 16.3 ms                                                | 10.9 ms: 1.49x faster                                                     |
| genshi_xml      | 66.0 ms                                                | 49.9 ms: 1.32x faster                                                     |
| Geometric mean  | (ref)                                                  | 1.46x faster                                                              |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250319-linux-x86_64-brandtbucher-jit_cached_consts-3.14.0a6+-32ebfed |
|--------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 171 us: 3.18x faster                                                      |
| generators               | 80.1 ms                                                | 27.8 ms: 2.88x faster                                                     |
| async_tree_io            | 1.77 sec                                               | 620 ms: 2.85x faster                                                      |
| async_tree_none          | 728 ms                                                 | 259 ms: 2.81x faster                                                      |
| async_tree_memoization   | 870 ms                                                 | 319 ms: 2.73x faster                                                      |
| deltablue                | 7.91 ms                                                | 3.01 ms: 2.63x faster                                                     |
| richards_super           | 94.7 ms                                                | 40.3 ms: 2.35x faster                                                     |
| richards                 | 79.3 ms                                                | 34.9 ms: 2.27x faster                                                     |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 496 ms: 2.05x faster                                                      |
| deepcopy_memo            | 58.5 us                                                | 29.4 us: 1.99x faster                                                     |
| pylint                   | 551 ms                                                 | 281 ms: 1.96x faster                                                      |
| chaos                    | 115 ms                                                 | 59.4 ms: 1.94x faster                                                     |
| logging_silent           | 190 ns                                                 | 98.1 ns: 1.93x faster                                                     |
| raytrace                 | 507 ms                                                 | 266 ms: 1.90x faster                                                      |
| scimark_sor              | 220 ms                                                 | 117 ms: 1.87x faster                                                      |
| deepcopy                 | 479 us                                                 | 256 us: 1.87x faster                                                      |
| go                       | 240 ms                                                 | 129 ms: 1.87x faster                                                      |
| float                    | 117 ms                                                 | 65.2 ms: 1.80x faster                                                     |
| spectral_norm            | 170 ms                                                 | 95.8 ms: 1.77x faster                                                     |
| nbody                    | 154 ms                                                 | 86.9 ms: 1.77x faster                                                     |
| scimark_monte_carlo      | 118 ms                                                 | 67.6 ms: 1.75x faster                                                     |
| tomli_loads              | 3.14 sec                                               | 1.86 sec: 1.69x faster                                                    |
| crypto_pyaes             | 128 ms                                                 | 78.2 ms: 1.63x faster                                                     |
| pyflate                  | 716 ms                                                 | 444 ms: 1.61x faster                                                      |
| unpickle_pure_python     | 331 us                                                 | 213 us: 1.55x faster                                                      |
| comprehensions           | 28.8 us                                                | 18.8 us: 1.53x faster                                                     |
| hexiom                   | 10.4 ms                                                | 6.79 ms: 1.53x faster                                                     |
| django_template          | 48.2 ms                                                | 31.6 ms: 1.53x faster                                                     |
| deepcopy_reduce          | 4.17 us                                                | 2.75 us: 1.51x faster                                                     |
| genshi_text              | 31.8 ms                                                | 21.0 ms: 1.51x faster                                                     |
| pickle_pure_python       | 484 us                                                 | 321 us: 1.51x faster                                                      |
| logging_simple           | 8.30 us                                                | 5.53 us: 1.50x faster                                                     |
| scimark_fft              | 466 ms                                                 | 311 ms: 1.50x faster                                                      |
| mako                     | 16.3 ms                                                | 10.9 ms: 1.49x faster                                                     |
| scimark_lu               | 176 ms                                                 | 118 ms: 1.49x faster                                                      |
| logging_format           | 9.09 us                                                | 6.16 us: 1.48x faster                                                     |
| regex_compile            | 188 ms                                                 | 128 ms: 1.48x faster                                                      |
| coroutines               | 35.1 ms                                                | 23.8 ms: 1.47x faster                                                     |
| xml_etree_process        | 79.1 ms                                                | 55.5 ms: 1.43x faster                                                     |
| html5lib                 | 88.9 ms                                                | 63.3 ms: 1.40x faster                                                     |
| dulwich_log              | 84.3 ms                                                | 60.9 ms: 1.38x faster                                                     |
| sqlalchemy_imperative    | 23.3 ms                                                | 16.9 ms: 1.38x faster                                                     |
| thrift                   | 1.07 ms                                                | 786 us: 1.36x faster                                                      |
| pycparser                | 1.58 sec                                               | 1.17 sec: 1.34x faster                                                    |
| pprint_pformat           | 2.10 sec                                               | 1.57 sec: 1.34x faster                                                    |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.86 ms: 1.33x faster                                                     |
| 2to3                     | 348 ms                                                 | 262 ms: 1.33x faster                                                      |
| pprint_safe_repr         | 1.02 sec                                               | 767 ms: 1.33x faster                                                      |
| genshi_xml               | 66.0 ms                                                | 49.9 ms: 1.32x faster                                                     |
| sqlalchemy_declarative   | 172 ms                                                 | 133 ms: 1.29x faster                                                      |
| nqueens                  | 106 ms                                                 | 84.1 ms: 1.26x faster                                                     |
| fannkuch                 | 532 ms                                                 | 424 ms: 1.25x faster                                                      |
| xml_etree_generate       | 99.4 ms                                                | 79.3 ms: 1.25x faster                                                     |
| json_dumps               | 14.2 ms                                                | 11.5 ms: 1.23x faster                                                     |
| pathlib                  | 20.5 ms                                                | 16.7 ms: 1.23x faster                                                     |
| docutils                 | 3.30 sec                                               | 2.69 sec: 1.23x faster                                                    |
| xml_etree_parse          | 168 ms                                                 | 140 ms: 1.20x faster                                                      |
| regex_v8                 | 27.8 ms                                                | 23.2 ms: 1.20x faster                                                     |
| xml_etree_iterparse      | 115 ms                                                 | 97.7 ms: 1.18x faster                                                     |
| mdp                      | 2.85 sec                                               | 2.48 sec: 1.15x faster                                                    |
| sqlite_synth             | 3.02 us                                                | 2.69 us: 1.12x faster                                                     |
| bench_thread_pool        | 986 us                                                 | 882 us: 1.12x faster                                                      |
| python_startup           | 14.6 ms                                                | 13.1 ms: 1.11x faster                                                     |
| meteor_contest           | 120 ms                                                 | 109 ms: 1.10x faster                                                      |
| json                     | 5.69 ms                                                | 5.29 ms: 1.08x faster                                                     |
| async_generators         | 444 ms                                                 | 421 ms: 1.05x faster                                                      |
| regex_effbot             | 3.63 ms                                                | 3.45 ms: 1.05x faster                                                     |
| json_loads               | 31.2 us                                                | 29.8 us: 1.05x faster                                                     |
| regex_dna                | 227 ms                                                 | 221 ms: 1.03x faster                                                      |
| pidigits                 | 191 ms                                                 | 186 ms: 1.03x faster                                                      |
| asyncio_websockets       | 559 ms                                                 | 551 ms: 1.01x faster                                                      |
| coverage                 | 79.4 ms                                                | 84.8 ms: 1.07x slower                                                     |
| telco                    | 7.27 ms                                                | 7.92 ms: 1.09x slower                                                     |
| gc_traversal             | 3.62 ms                                                | 4.83 ms: 1.33x slower                                                     |
| python_startup_no_site   | 5.93 ms                                                | 8.20 ms: 1.38x slower                                                     |
| create_gc_cycles         | 1.62 ms                                                | 2.50 ms: 1.54x slower                                                     |
| bench_mp_pool            | 24.0 ms                                                | 82.8 ms: 3.45x slower                                                     |
| Geometric mean           | (ref)                                                  | 1.42x faster                                                              |
Ignored benchmarks (24) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, sympy_expand, sympy_integrate, sympy_str, sympy_sum, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (15) of results/bm-20250319-3.14.0a6+-32ebfed-JIT/bm-20250319-linux-x86_64-brandtbucher-jit_cached_consts-3.14.0a6+-32ebfed.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.455x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.34x
- 95% likely to have a speedup of 1.33x
- 99% likely to have a speedup of 1.31x

# Memory
- memory change: 1.29x