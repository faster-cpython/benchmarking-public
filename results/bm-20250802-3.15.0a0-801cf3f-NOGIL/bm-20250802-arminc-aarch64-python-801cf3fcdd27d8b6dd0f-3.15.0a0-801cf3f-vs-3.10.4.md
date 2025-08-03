# Results vs. 3.10.4

- fork: python
- ref: 801cf3fcdd27d8b6dd0f
- machine: linux-aarch64
- commit hash: 801cf3f
- commit date: 2025-08-02
- overall geometric mean: 1.146x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.08x faster
- Memory change: 1.67x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250802-arminc-aarch64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 381 ms                                                                | 350 ms: 1.09x faster                                                    |
| docutils       | 3.53 sec                                                              | 3.16 sec: 1.12x faster                                                  |
| html5lib       | 86.5 ms                                                               | 70.0 ms: 1.23x faster                                                   |
| Geometric mean | (ref)                                                                 | 1.14x faster                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250802-arminc-aarch64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f |
|-------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_io           | 2.28 sec                                                              | 846 ms: 2.70x faster                                                    |
| async_tree_none         | 950 ms                                                                | 390 ms: 2.43x faster                                                    |
| async_tree_memoization  | 1.13 sec                                                              | 470 ms: 2.41x faster                                                    |
| async_tree_cpu_io_mixed | 1.27 sec                                                              | 657 ms: 1.94x faster                                                    |
| Geometric mean          | (ref)                                                                 | 2.35x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250802-arminc-aarch64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 135 ms                                                                | 94.0 ms: 1.43x faster                                                   |
| nbody          | 166 ms                                                                | 183 ms: 1.10x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.09x faster                                                            |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250802-arminc-aarch64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_v8       | 32.2 ms                                                               | 25.9 ms: 1.24x faster                                                   |
| regex_compile  | 177 ms                                                                | 153 ms: 1.16x faster                                                    |
| regex_effbot   | 4.25 ms                                                               | 3.83 ms: 1.11x faster                                                   |
| regex_dna      | 257 ms                                                                | 238 ms: 1.08x faster                                                    |
| Geometric mean | (ref)                                                                 | 1.15x faster                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250802-arminc-aarch64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f |
|----------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| unpickle_pure_python | 366 us                                                                | 300 us: 1.22x faster                                                    |
| xml_etree_iterparse  | 156 ms                                                                | 130 ms: 1.20x faster                                                    |
| pickle_pure_python   | 529 us                                                                | 442 us: 1.20x faster                                                    |
| tomli_loads          | 3.36 sec                                                              | 2.86 sec: 1.18x faster                                                  |
| xml_etree_parse      | 212 ms                                                                | 186 ms: 1.14x faster                                                    |
| json_dumps           | 16.7 ms                                                               | 14.9 ms: 1.12x faster                                                   |
| unpickle_list        | 6.99 us                                                               | 6.87 us: 1.02x faster                                                   |
| xml_etree_process    | 99.5 ms                                                               | 101 ms: 1.01x slower                                                    |
| pickle_dict          | 35.1 us                                                               | 38.8 us: 1.11x slower                                                   |
| pickle_list          | 5.24 us                                                               | 5.83 us: 1.11x slower                                                   |
| xml_etree_generate   | 123 ms                                                                | 139 ms: 1.13x slower                                                    |
| unpickle             | 17.5 us                                                               | 20.1 us: 1.15x slower                                                   |
| json_loads           | 30.9 us                                                               | 36.6 us: 1.18x slower                                                   |
| pickle               | 12.5 us                                                               | 15.3 us: 1.22x slower                                                   |
| Geometric mean       | (ref)                                                                 | 1.01x faster                                                            |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250802-arminc-aarch64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f |
|------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup_no_site | 6.89 ms                                                               | 12.0 ms: 1.74x slower                                                   |
| python_startup         | 11.2 ms                                                               | 19.9 ms: 1.78x slower                                                   |
| Geometric mean         | (ref)                                                                 | 1.76x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250802-arminc-aarch64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f |
|-----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| django_template | 53.3 ms                                                               | 50.9 ms: 1.05x faster                                                   |
| genshi_xml      | 69.8 ms                                                               | 76.0 ms: 1.09x slower                                                   |
| mako            | 18.9 ms                                                               | 21.4 ms: 1.13x slower                                                   |
| Geometric mean  | (ref)                                                                 | 1.05x slower                                                            |

Benchmark hidden because not significant (1): genshi_text

All benchmarks:
===============

| Benchmark                | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250802-arminc-aarch64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f |
|--------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| typing_runtime_protocols | 661 us                                                                | 244 us: 2.71x faster                                                    |
| async_tree_io            | 2.28 sec                                                              | 846 ms: 2.70x faster                                                    |
| async_tree_none          | 950 ms                                                                | 390 ms: 2.43x faster                                                    |
| async_tree_memoization   | 1.13 sec                                                              | 470 ms: 2.41x faster                                                    |
| async_tree_cpu_io_mixed  | 1.27 sec                                                              | 657 ms: 1.94x faster                                                    |
| mdp                      | 3.70 sec                                                              | 1.93 sec: 1.92x faster                                                  |
| deltablue                | 8.94 ms                                                               | 4.80 ms: 1.86x faster                                                   |
| go                       | 264 ms                                                                | 152 ms: 1.74x faster                                                    |
| asyncio_tcp              | 944 ms                                                                | 559 ms: 1.69x faster                                                    |
| generators               | 68.1 ms                                                               | 40.7 ms: 1.67x faster                                                   |
| logging_silent           | 222 ns                                                                | 139 ns: 1.60x faster                                                    |
| scimark_sor              | 246 ms                                                                | 162 ms: 1.52x faster                                                    |
| chaos                    | 121 ms                                                                | 82.0 ms: 1.48x faster                                                   |
| gc_traversal             | 4.15 ms                                                               | 2.87 ms: 1.45x faster                                                   |
| raytrace                 | 573 ms                                                                | 398 ms: 1.44x faster                                                    |
| float                    | 135 ms                                                                | 94.0 ms: 1.43x faster                                                   |
| hexiom                   | 10.9 ms                                                               | 7.77 ms: 1.40x faster                                                   |
| comprehensions           | 33.1 us                                                               | 24.1 us: 1.38x faster                                                   |
| deepcopy_memo            | 61.7 us                                                               | 45.3 us: 1.36x faster                                                   |
| pyflate                  | 795 ms                                                                | 584 ms: 1.36x faster                                                    |
| asyncio_tcp_ssl          | 3.28 sec                                                              | 2.43 sec: 1.35x faster                                                  |
| richards_super           | 107 ms                                                                | 80.3 ms: 1.34x faster                                                   |
| deepcopy                 | 511 us                                                                | 386 us: 1.32x faster                                                    |
| pylint                   | 485 ms                                                                | 373 ms: 1.30x faster                                                    |
| richards                 | 91.7 ms                                                               | 70.7 ms: 1.30x faster                                                   |
| spectral_norm            | 186 ms                                                                | 144 ms: 1.29x faster                                                    |
| pycparser                | 1.69 sec                                                              | 1.33 sec: 1.27x faster                                                  |
| crypto_pyaes             | 134 ms                                                                | 107 ms: 1.25x faster                                                    |
| regex_v8                 | 32.2 ms                                                               | 25.9 ms: 1.24x faster                                                   |
| dulwich_log              | 73.5 ms                                                               | 59.1 ms: 1.24x faster                                                   |
| scimark_monte_carlo      | 128 ms                                                                | 103 ms: 1.24x faster                                                    |
| html5lib                 | 86.5 ms                                                               | 70.0 ms: 1.23x faster                                                   |
| unpickle_pure_python     | 366 us                                                                | 300 us: 1.22x faster                                                    |
| scimark_lu               | 227 ms                                                                | 186 ms: 1.22x faster                                                    |
| xml_etree_iterparse      | 156 ms                                                                | 130 ms: 1.20x faster                                                    |
| pickle_pure_python       | 529 us                                                                | 442 us: 1.20x faster                                                    |
| sqlite_synth             | 4.12 us                                                               | 3.44 us: 1.20x faster                                                   |
| logging_simple           | 9.78 us                                                               | 8.24 us: 1.19x faster                                                   |
| coroutines               | 37.2 ms                                                               | 31.6 ms: 1.18x faster                                                   |
| tomli_loads              | 3.36 sec                                                              | 2.86 sec: 1.18x faster                                                  |
| pathlib                  | 26.3 ms                                                               | 22.6 ms: 1.16x faster                                                   |
| regex_compile            | 177 ms                                                                | 153 ms: 1.16x faster                                                    |
| logging_format           | 10.6 us                                                               | 9.21 us: 1.15x faster                                                   |
| xml_etree_parse          | 212 ms                                                                | 186 ms: 1.14x faster                                                    |
| json_dumps               | 16.7 ms                                                               | 14.9 ms: 1.12x faster                                                   |
| docutils                 | 3.53 sec                                                              | 3.16 sec: 1.12x faster                                                  |
| regex_effbot             | 4.25 ms                                                               | 3.83 ms: 1.11x faster                                                   |
| pprint_pformat           | 2.36 sec                                                              | 2.14 sec: 1.10x faster                                                  |
| pprint_safe_repr         | 1.15 sec                                                              | 1.04 sec: 1.10x faster                                                  |
| 2to3                     | 381 ms                                                                | 350 ms: 1.09x faster                                                    |
| regex_dna                | 257 ms                                                                | 238 ms: 1.08x faster                                                    |
| scimark_fft              | 500 ms                                                                | 466 ms: 1.07x faster                                                    |
| django_template          | 53.3 ms                                                               | 50.9 ms: 1.05x faster                                                   |
| deepcopy_reduce          | 4.60 us                                                               | 4.39 us: 1.05x faster                                                   |
| thrift                   | 1.26 ms                                                               | 1.20 ms: 1.05x faster                                                   |
| sympy_integrate          | 26.5 ms                                                               | 25.6 ms: 1.04x faster                                                   |
| unpickle_list            | 6.99 us                                                               | 6.87 us: 1.02x faster                                                   |
| nqueens                  | 117 ms                                                                | 116 ms: 1.01x faster                                                    |
| xml_etree_process        | 99.5 ms                                                               | 101 ms: 1.01x slower                                                    |
| asyncio_websockets       | 657 ms                                                                | 667 ms: 1.02x slower                                                    |
| sympy_str                | 329 ms                                                                | 337 ms: 1.02x slower                                                    |
| json                     | 5.88 ms                                                               | 6.25 ms: 1.06x slower                                                   |
| fannkuch                 | 546 ms                                                                | 588 ms: 1.08x slower                                                    |
| sympy_expand             | 543 ms                                                                | 586 ms: 1.08x slower                                                    |
| genshi_xml               | 69.8 ms                                                               | 76.0 ms: 1.09x slower                                                   |
| nbody                    | 166 ms                                                                | 183 ms: 1.10x slower                                                    |
| meteor_contest           | 126 ms                                                                | 139 ms: 1.10x slower                                                    |
| pickle_dict              | 35.1 us                                                               | 38.8 us: 1.11x slower                                                   |
| pickle_list              | 5.24 us                                                               | 5.83 us: 1.11x slower                                                   |
| bench_thread_pool        | 1.59 ms                                                               | 1.80 ms: 1.13x slower                                                   |
| xml_etree_generate       | 123 ms                                                                | 139 ms: 1.13x slower                                                    |
| mako                     | 18.9 ms                                                               | 21.4 ms: 1.13x slower                                                   |
| async_generators         | 452 ms                                                                | 519 ms: 1.15x slower                                                    |
| unpickle                 | 17.5 us                                                               | 20.1 us: 1.15x slower                                                   |
| json_loads               | 30.9 us                                                               | 36.6 us: 1.18x slower                                                   |
| pickle                   | 12.5 us                                                               | 15.3 us: 1.22x slower                                                   |
| coverage                 | 83.6 ms                                                               | 142 ms: 1.70x slower                                                    |
| python_startup_no_site   | 6.89 ms                                                               | 12.0 ms: 1.74x slower                                                   |
| python_startup           | 11.2 ms                                                               | 19.9 ms: 1.78x slower                                                   |
| bench_mp_pool            | 14.5 ms                                                               | 63.8 ms: 4.39x slower                                                   |
| telco                    | 8.49 ms                                                               | 186 ms: 21.97x slower                                                   |
| Geometric mean           | (ref)                                                                 | 1.11x faster                                                            |

Benchmark hidden because not significant (5): pidigits, create_gc_cycles, sympy_sum, scimark_sparse_mat_mult, genshi_text
Ignored benchmarks (13) of results/bm-20220323-3.10.4-9d38120/bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (16) of results/bm-20250802-3.15.0a0-801cf3f-NOGIL/bm-20250802-arminc-aarch64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, unpack_sequence

- Geometric mean (including insignificant results): 1.146x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.10x
- 95% likely to have a speedup of 1.10x
- 99% likely to have a speedup of 1.08x

# Memory
- memory change: 1.67x