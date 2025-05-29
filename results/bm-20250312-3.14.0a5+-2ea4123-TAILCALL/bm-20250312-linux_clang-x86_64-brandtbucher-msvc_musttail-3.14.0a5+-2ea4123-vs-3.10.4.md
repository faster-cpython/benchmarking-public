# Results vs. 3.10.4

- fork: brandtbucher
- ref: msvc_musttail
- machine: linux-x86_64
- commit hash: 2ea4123
- commit date: 2025-03-12
- overall geometric mean: 1.486x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.35x faster
- Memory change: 1.28x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250312-linux-x86_64-brandtbucher-msvc_musttail-3.14.0a5+-2ea4123 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 251 ms: 1.39x faster                                                  |
| docutils       | 3.30 sec                                               | 2.61 sec: 1.26x faster                                                |
| html5lib       | 88.9 ms                                                | 57.3 ms: 1.55x faster                                                 |
| Geometric mean | (ref)                                                  | 1.40x faster                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250312-linux-x86_64-brandtbucher-msvc_musttail-3.14.0a5+-2ea4123 |
|-------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_io           | 1.77 sec                                               | 596 ms: 2.97x faster                                                  |
| async_tree_none         | 728 ms                                                 | 249 ms: 2.92x faster                                                  |
| async_tree_memoization  | 870 ms                                                 | 306 ms: 2.84x faster                                                  |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 517 ms: 1.97x faster                                                  |
| Geometric mean          | (ref)                                                  | 2.64x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250312-linux-x86_64-brandtbucher-msvc_musttail-3.14.0a5+-2ea4123 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 86.4 ms: 1.78x faster                                                 |
| float          | 117 ms                                                 | 66.8 ms: 1.75x faster                                                 |
| pidigits       | 191 ms                                                 | 219 ms: 1.15x slower                                                  |
| Geometric mean | (ref)                                                  | 1.39x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250312-linux-x86_64-brandtbucher-msvc_musttail-3.14.0a5+-2ea4123 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 125 ms: 1.51x faster                                                  |
| regex_v8       | 27.8 ms                                                | 23.8 ms: 1.17x faster                                                 |
| regex_dna      | 227 ms                                                 | 196 ms: 1.16x faster                                                  |
| regex_effbot   | 3.63 ms                                                | 3.28 ms: 1.11x faster                                                 |
| Geometric mean | (ref)                                                  | 1.23x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250312-linux-x86_64-brandtbucher-msvc_musttail-3.14.0a5+-2ea4123 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| tomli_loads          | 3.14 sec                                               | 1.88 sec: 1.67x faster                                                |
| pickle_pure_python   | 484 us                                                 | 306 us: 1.58x faster                                                  |
| unpickle_pure_python | 331 us                                                 | 217 us: 1.52x faster                                                  |
| xml_etree_process    | 79.1 ms                                                | 58.7 ms: 1.35x faster                                                 |
| xml_etree_generate   | 99.4 ms                                                | 86.8 ms: 1.14x faster                                                 |
| json_dumps           | 14.2 ms                                                | 12.5 ms: 1.14x faster                                                 |
| xml_etree_iterparse  | 115 ms                                                 | 103 ms: 1.12x faster                                                  |
| json_loads           | 31.2 us                                                | 28.9 us: 1.08x faster                                                 |
| xml_etree_parse      | 168 ms                                                 | 163 ms: 1.03x faster                                                  |
| Geometric mean       | (ref)                                                  | 1.27x faster                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250312-linux-x86_64-brandtbucher-msvc_musttail-3.14.0a5+-2ea4123 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 12.7 ms: 1.15x faster                                                 |
| python_startup_no_site | 5.93 ms                                                | 7.02 ms: 1.18x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.02x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250312-linux-x86_64-brandtbucher-msvc_musttail-3.14.0a5+-2ea4123 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| django_template | 48.2 ms                                                | 30.6 ms: 1.58x faster                                                 |
| genshi_text     | 31.8 ms                                                | 21.2 ms: 1.50x faster                                                 |
| mako            | 16.3 ms                                                | 11.6 ms: 1.41x faster                                                 |
| genshi_xml      | 66.0 ms                                                | 48.1 ms: 1.37x faster                                                 |
| Geometric mean  | (ref)                                                  | 1.46x faster                                                          |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250312-linux-x86_64-brandtbucher-msvc_musttail-3.14.0a5+-2ea4123 |
|--------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 148 us: 3.69x faster                                                  |
| async_tree_io            | 1.77 sec                                               | 596 ms: 2.97x faster                                                  |
| async_tree_none          | 728 ms                                                 | 249 ms: 2.92x faster                                                  |
| async_tree_memoization   | 870 ms                                                 | 306 ms: 2.84x faster                                                  |
| generators               | 80.1 ms                                                | 28.6 ms: 2.80x faster                                                 |
| deltablue                | 7.91 ms                                                | 3.01 ms: 2.63x faster                                                 |
| logging_silent           | 190 ns                                                 | 87.1 ns: 2.18x faster                                                 |
| chaos                    | 115 ms                                                 | 53.3 ms: 2.16x faster                                                 |
| go                       | 240 ms                                                 | 113 ms: 2.13x faster                                                  |
| scimark_sor              | 220 ms                                                 | 107 ms: 2.06x faster                                                  |
| spectral_norm            | 170 ms                                                 | 82.5 ms: 2.06x faster                                                 |
| pylint                   | 551 ms                                                 | 275 ms: 2.00x faster                                                  |
| raytrace                 | 507 ms                                                 | 255 ms: 1.99x faster                                                  |
| deepcopy_memo            | 58.5 us                                                | 29.4 us: 1.99x faster                                                 |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 517 ms: 1.97x faster                                                  |
| scimark_monte_carlo      | 118 ms                                                 | 60.1 ms: 1.97x faster                                                 |
| deepcopy                 | 479 us                                                 | 244 us: 1.96x faster                                                  |
| comprehensions           | 28.8 us                                                | 15.5 us: 1.85x faster                                                 |
| hexiom                   | 10.4 ms                                                | 5.74 ms: 1.81x faster                                                 |
| nbody                    | 154 ms                                                 | 86.4 ms: 1.78x faster                                                 |
| crypto_pyaes             | 128 ms                                                 | 72.5 ms: 1.76x faster                                                 |
| float                    | 117 ms                                                 | 66.8 ms: 1.75x faster                                                 |
| pyflate                  | 716 ms                                                 | 410 ms: 1.75x faster                                                  |
| richards_super           | 94.7 ms                                                | 55.6 ms: 1.70x faster                                                 |
| tomli_loads              | 3.14 sec                                               | 1.88 sec: 1.67x faster                                                |
| richards                 | 79.3 ms                                                | 47.4 ms: 1.67x faster                                                 |
| scimark_lu               | 176 ms                                                 | 107 ms: 1.65x faster                                                  |
| deepcopy_reduce          | 4.17 us                                                | 2.53 us: 1.65x faster                                                 |
| scimark_fft              | 466 ms                                                 | 289 ms: 1.61x faster                                                  |
| coroutines               | 35.1 ms                                                | 22.1 ms: 1.59x faster                                                 |
| pickle_pure_python       | 484 us                                                 | 306 us: 1.58x faster                                                  |
| logging_simple           | 8.30 us                                                | 5.26 us: 1.58x faster                                                 |
| django_template          | 48.2 ms                                                | 30.6 ms: 1.58x faster                                                 |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.14 ms: 1.56x faster                                                 |
| logging_format           | 9.09 us                                                | 5.86 us: 1.55x faster                                                 |
| html5lib                 | 88.9 ms                                                | 57.3 ms: 1.55x faster                                                 |
| unpickle_pure_python     | 331 us                                                 | 217 us: 1.52x faster                                                  |
| regex_compile            | 188 ms                                                 | 125 ms: 1.51x faster                                                  |
| genshi_text              | 31.8 ms                                                | 21.2 ms: 1.50x faster                                                 |
| thrift                   | 1.07 ms                                                | 737 us: 1.45x faster                                                  |
| sqlalchemy_imperative    | 23.3 ms                                                | 16.1 ms: 1.45x faster                                                 |
| mako                     | 16.3 ms                                                | 11.6 ms: 1.41x faster                                                 |
| nqueens                  | 106 ms                                                 | 75.4 ms: 1.40x faster                                                 |
| pprint_pformat           | 2.10 sec                                               | 1.51 sec: 1.40x faster                                                |
| 2to3                     | 348 ms                                                 | 251 ms: 1.39x faster                                                  |
| pprint_safe_repr         | 1.02 sec                                               | 736 ms: 1.38x faster                                                  |
| sympy_sum                | 196 ms                                                 | 143 ms: 1.38x faster                                                  |
| pathlib                  | 20.5 ms                                                | 14.9 ms: 1.37x faster                                                 |
| genshi_xml               | 66.0 ms                                                | 48.1 ms: 1.37x faster                                                 |
| sqlalchemy_declarative   | 172 ms                                                 | 126 ms: 1.37x faster                                                  |
| sympy_integrate          | 25.8 ms                                                | 18.9 ms: 1.36x faster                                                 |
| pycparser                | 1.58 sec                                               | 1.16 sec: 1.36x faster                                                |
| dulwich_log              | 84.3 ms                                                | 61.8 ms: 1.36x faster                                                 |
| fannkuch                 | 532 ms                                                 | 393 ms: 1.35x faster                                                  |
| xml_etree_process        | 79.1 ms                                                | 58.7 ms: 1.35x faster                                                 |
| sympy_str                | 346 ms                                                 | 258 ms: 1.34x faster                                                  |
| sympy_expand             | 566 ms                                                 | 440 ms: 1.29x faster                                                  |
| docutils                 | 3.30 sec                                               | 2.61 sec: 1.26x faster                                                |
| async_generators         | 444 ms                                                 | 368 ms: 1.21x faster                                                  |
| bench_thread_pool        | 986 us                                                 | 831 us: 1.19x faster                                                  |
| regex_v8                 | 27.8 ms                                                | 23.8 ms: 1.17x faster                                                 |
| regex_dna                | 227 ms                                                 | 196 ms: 1.16x faster                                                  |
| python_startup           | 14.6 ms                                                | 12.7 ms: 1.15x faster                                                 |
| xml_etree_generate       | 99.4 ms                                                | 86.8 ms: 1.14x faster                                                 |
| sqlite_synth             | 3.02 us                                                | 2.66 us: 1.14x faster                                                 |
| json_dumps               | 14.2 ms                                                | 12.5 ms: 1.14x faster                                                 |
| xml_etree_iterparse      | 115 ms                                                 | 103 ms: 1.12x faster                                                  |
| regex_effbot             | 3.63 ms                                                | 3.28 ms: 1.11x faster                                                 |
| meteor_contest           | 120 ms                                                 | 111 ms: 1.08x faster                                                  |
| json_loads               | 31.2 us                                                | 28.9 us: 1.08x faster                                                 |
| json                     | 5.69 ms                                                | 5.28 ms: 1.08x faster                                                 |
| mdp                      | 2.85 sec                                               | 2.65 sec: 1.08x faster                                                |
| xml_etree_parse          | 168 ms                                                 | 163 ms: 1.03x faster                                                  |
| asyncio_websockets       | 559 ms                                                 | 551 ms: 1.01x faster                                                  |
| telco                    | 7.27 ms                                                | 7.39 ms: 1.02x slower                                                 |
| pidigits                 | 191 ms                                                 | 219 ms: 1.15x slower                                                  |
| python_startup_no_site   | 5.93 ms                                                | 7.02 ms: 1.18x slower                                                 |
| gc_traversal             | 3.62 ms                                                | 4.97 ms: 1.37x slower                                                 |
| create_gc_cycles         | 1.62 ms                                                | 2.54 ms: 1.57x slower                                                 |
| bench_mp_pool            | 24.0 ms                                                | 80.9 ms: 3.37x slower                                                 |
| Geometric mean           | (ref)                                                  | 1.46x faster                                                          |

Benchmark hidden because not significant (1): coverage
Ignored benchmarks (20) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (15) of results/bm-20250312-3.14.0a5+-2ea4123-CLANG/bm-20250312-linux-x86_64-brandtbucher-msvc_musttail-3.14.0a5+-2ea4123.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.486x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.38x
- 95% likely to have a speedup of 1.37x
- 99% likely to have a speedup of 1.35x

# Memory
- memory change: 1.28x