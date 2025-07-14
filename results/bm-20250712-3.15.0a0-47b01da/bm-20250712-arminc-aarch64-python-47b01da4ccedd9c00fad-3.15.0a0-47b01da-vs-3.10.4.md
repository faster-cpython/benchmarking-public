# Results vs. 3.10.4

- fork: python
- ref: 47b01da4ccedd9c00fad
- machine: linux-aarch64
- commit hash: 47b01da
- commit date: 2025-07-12
- overall geometric mean: 1.305x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.24x faster
- Memory change: 1.38x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250712-arminc-aarch64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 381 ms                                                                | 300 ms: 1.27x faster                                                    |
| docutils       | 3.53 sec                                                              | 2.93 sec: 1.20x faster                                                  |
| html5lib       | 86.5 ms                                                               | 61.5 ms: 1.41x faster                                                   |
| Geometric mean | (ref)                                                                 | 1.29x faster                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250712-arminc-aarch64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da |
|-------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_io           | 2.28 sec                                                              | 872 ms: 2.62x faster                                                    |
| async_tree_none         | 950 ms                                                                | 374 ms: 2.54x faster                                                    |
| async_tree_memoization  | 1.13 sec                                                              | 473 ms: 2.39x faster                                                    |
| async_tree_cpu_io_mixed | 1.27 sec                                                              | 659 ms: 1.93x faster                                                    |
| Geometric mean          | (ref)                                                                 | 2.36x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250712-arminc-aarch64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 135 ms                                                                | 85.3 ms: 1.58x faster                                                   |
| nbody          | 166 ms                                                                | 123 ms: 1.35x faster                                                    |
| pidigits       | 235 ms                                                                | 236 ms: 1.00x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.29x faster                                                            |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250712-arminc-aarch64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                                | 122 ms: 1.45x faster                                                    |
| regex_dna      | 257 ms                                                                | 221 ms: 1.16x faster                                                    |
| regex_v8       | 32.2 ms                                                               | 28.6 ms: 1.13x faster                                                   |
| regex_effbot   | 4.25 ms                                                               | 3.85 ms: 1.10x faster                                                   |
| Geometric mean | (ref)                                                                 | 1.20x faster                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250712-arminc-aarch64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da |
|----------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| unpickle_pure_python | 366 us                                                                | 261 us: 1.40x faster                                                    |
| tomli_loads          | 3.36 sec                                                              | 2.45 sec: 1.37x faster                                                  |
| pickle_pure_python   | 529 us                                                                | 393 us: 1.35x faster                                                    |
| xml_etree_process    | 99.5 ms                                                               | 78.8 ms: 1.26x faster                                                   |
| json_dumps           | 16.7 ms                                                               | 14.2 ms: 1.18x faster                                                   |
| xml_etree_parse      | 212 ms                                                                | 181 ms: 1.17x faster                                                    |
| xml_etree_generate   | 123 ms                                                                | 111 ms: 1.11x faster                                                    |
| xml_etree_iterparse  | 156 ms                                                                | 142 ms: 1.10x faster                                                    |
| unpickle_list        | 6.99 us                                                               | 6.55 us: 1.07x faster                                                   |
| json_loads           | 30.9 us                                                               | 32.8 us: 1.06x slower                                                   |
| unpickle             | 17.5 us                                                               | 18.7 us: 1.07x slower                                                   |
| pickle_dict          | 35.1 us                                                               | 38.6 us: 1.10x slower                                                   |
| pickle_list          | 5.24 us                                                               | 5.86 us: 1.12x slower                                                   |
| pickle               | 12.5 us                                                               | 15.5 us: 1.25x slower                                                   |
| Geometric mean       | (ref)                                                                 | 1.09x faster                                                            |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250712-arminc-aarch64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da |
|------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup_no_site | 6.89 ms                                                               | 8.59 ms: 1.25x slower                                                   |
| python_startup         | 11.2 ms                                                               | 15.0 ms: 1.34x slower                                                   |
| Geometric mean         | (ref)                                                                 | 1.29x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250712-arminc-aarch64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da |
|-----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mako            | 18.9 ms                                                               | 13.6 ms: 1.39x faster                                                   |
| genshi_text     | 35.2 ms                                                               | 27.1 ms: 1.30x faster                                                   |
| django_template | 53.3 ms                                                               | 41.7 ms: 1.28x faster                                                   |
| genshi_xml      | 69.8 ms                                                               | 59.7 ms: 1.17x faster                                                   |
| Geometric mean  | (ref)                                                                 | 1.28x faster                                                            |

All benchmarks:
===============

| Benchmark                | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250712-arminc-aarch64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da |
|--------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| typing_runtime_protocols | 661 us                                                                | 193 us: 3.42x faster                                                    |
| async_tree_io            | 2.28 sec                                                              | 872 ms: 2.62x faster                                                    |
| async_tree_none          | 950 ms                                                                | 374 ms: 2.54x faster                                                    |
| async_tree_memoization   | 1.13 sec                                                              | 473 ms: 2.39x faster                                                    |
| deltablue                | 8.94 ms                                                               | 4.00 ms: 2.24x faster                                                   |
| mdp                      | 3.70 sec                                                              | 1.68 sec: 2.20x faster                                                  |
| go                       | 264 ms                                                                | 127 ms: 2.09x faster                                                    |
| async_tree_cpu_io_mixed  | 1.27 sec                                                              | 659 ms: 1.93x faster                                                    |
| generators               | 68.1 ms                                                               | 35.4 ms: 1.92x faster                                                   |
| chaos                    | 121 ms                                                                | 66.7 ms: 1.82x faster                                                   |
| raytrace                 | 573 ms                                                                | 326 ms: 1.76x faster                                                    |
| richards                 | 91.7 ms                                                               | 52.2 ms: 1.76x faster                                                   |
| richards_super           | 107 ms                                                                | 61.5 ms: 1.74x faster                                                   |
| asyncio_tcp              | 944 ms                                                                | 543 ms: 1.74x faster                                                    |
| logging_silent           | 222 ns                                                                | 129 ns: 1.72x faster                                                    |
| scimark_sor              | 246 ms                                                                | 145 ms: 1.70x faster                                                    |
| deepcopy_memo            | 61.7 us                                                               | 37.2 us: 1.66x faster                                                   |
| comprehensions           | 33.1 us                                                               | 20.0 us: 1.65x faster                                                   |
| hexiom                   | 10.9 ms                                                               | 6.79 ms: 1.61x faster                                                   |
| scimark_monte_carlo      | 128 ms                                                                | 80.3 ms: 1.59x faster                                                   |
| deepcopy                 | 511 us                                                                | 321 us: 1.59x faster                                                    |
| crypto_pyaes             | 134 ms                                                                | 84.6 ms: 1.58x faster                                                   |
| float                    | 135 ms                                                                | 85.3 ms: 1.58x faster                                                   |
| spectral_norm            | 186 ms                                                                | 118 ms: 1.57x faster                                                    |
| scimark_lu               | 227 ms                                                                | 146 ms: 1.55x faster                                                    |
| pyflate                  | 795 ms                                                                | 522 ms: 1.52x faster                                                    |
| pylint                   | 485 ms                                                                | 319 ms: 1.52x faster                                                    |
| asyncio_tcp_ssl          | 3.28 sec                                                              | 2.16 sec: 1.52x faster                                                  |
| regex_compile            | 177 ms                                                                | 122 ms: 1.45x faster                                                    |
| html5lib                 | 86.5 ms                                                               | 61.5 ms: 1.41x faster                                                   |
| unpickle_pure_python     | 366 us                                                                | 261 us: 1.40x faster                                                    |
| mako                     | 18.9 ms                                                               | 13.6 ms: 1.39x faster                                                   |
| dulwich_log              | 73.5 ms                                                               | 52.8 ms: 1.39x faster                                                   |
| logging_format           | 10.6 us                                                               | 7.65 us: 1.39x faster                                                   |
| logging_simple           | 9.78 us                                                               | 7.12 us: 1.37x faster                                                   |
| tomli_loads              | 3.36 sec                                                              | 2.45 sec: 1.37x faster                                                  |
| nbody                    | 166 ms                                                                | 123 ms: 1.35x faster                                                    |
| pycparser                | 1.69 sec                                                              | 1.26 sec: 1.35x faster                                                  |
| pickle_pure_python       | 529 us                                                                | 393 us: 1.35x faster                                                    |
| thrift                   | 1.26 ms                                                               | 946 us: 1.33x faster                                                    |
| sympy_sum                | 184 ms                                                                | 141 ms: 1.31x faster                                                    |
| sympy_integrate          | 26.5 ms                                                               | 20.3 ms: 1.30x faster                                                   |
| pprint_pformat           | 2.36 sec                                                              | 1.82 sec: 1.30x faster                                                  |
| genshi_text              | 35.2 ms                                                               | 27.1 ms: 1.30x faster                                                   |
| pprint_safe_repr         | 1.15 sec                                                              | 884 ms: 1.30x faster                                                    |
| deepcopy_reduce          | 4.60 us                                                               | 3.55 us: 1.29x faster                                                   |
| django_template          | 53.3 ms                                                               | 41.7 ms: 1.28x faster                                                   |
| 2to3                     | 381 ms                                                                | 300 ms: 1.27x faster                                                    |
| xml_etree_process        | 99.5 ms                                                               | 78.8 ms: 1.26x faster                                                   |
| coroutines               | 37.2 ms                                                               | 29.6 ms: 1.25x faster                                                   |
| nqueens                  | 117 ms                                                                | 97.1 ms: 1.21x faster                                                   |
| docutils                 | 3.53 sec                                                              | 2.93 sec: 1.20x faster                                                  |
| sympy_str                | 329 ms                                                                | 273 ms: 1.20x faster                                                    |
| sympy_expand             | 543 ms                                                                | 460 ms: 1.18x faster                                                    |
| json_dumps               | 16.7 ms                                                               | 14.2 ms: 1.18x faster                                                   |
| scimark_fft              | 500 ms                                                                | 427 ms: 1.17x faster                                                    |
| meteor_contest           | 126 ms                                                                | 108 ms: 1.17x faster                                                    |
| genshi_xml               | 69.8 ms                                                               | 59.7 ms: 1.17x faster                                                   |
| xml_etree_parse          | 212 ms                                                                | 181 ms: 1.17x faster                                                    |
| fannkuch                 | 546 ms                                                                | 467 ms: 1.17x faster                                                    |
| bench_thread_pool        | 1.59 ms                                                               | 1.36 ms: 1.17x faster                                                   |
| regex_dna                | 257 ms                                                                | 221 ms: 1.16x faster                                                    |
| regex_v8                 | 32.2 ms                                                               | 28.6 ms: 1.13x faster                                                   |
| pathlib                  | 26.3 ms                                                               | 23.6 ms: 1.12x faster                                                   |
| xml_etree_generate       | 123 ms                                                                | 111 ms: 1.11x faster                                                    |
| scimark_sparse_mat_mult  | 7.62 ms                                                               | 6.90 ms: 1.11x faster                                                   |
| regex_effbot             | 4.25 ms                                                               | 3.85 ms: 1.10x faster                                                   |
| xml_etree_iterparse      | 156 ms                                                                | 142 ms: 1.10x faster                                                    |
| sqlite_synth             | 4.12 us                                                               | 3.80 us: 1.08x faster                                                   |
| unpickle_list            | 6.99 us                                                               | 6.55 us: 1.07x faster                                                   |
| json                     | 5.88 ms                                                               | 5.74 ms: 1.02x faster                                                   |
| pidigits                 | 235 ms                                                                | 236 ms: 1.00x slower                                                    |
| asyncio_websockets       | 657 ms                                                                | 673 ms: 1.02x slower                                                    |
| json_loads               | 30.9 us                                                               | 32.8 us: 1.06x slower                                                   |
| unpickle                 | 17.5 us                                                               | 18.7 us: 1.07x slower                                                   |
| pickle_dict              | 35.1 us                                                               | 38.6 us: 1.10x slower                                                   |
| pickle_list              | 5.24 us                                                               | 5.86 us: 1.12x slower                                                   |
| pickle                   | 12.5 us                                                               | 15.5 us: 1.25x slower                                                   |
| python_startup_no_site   | 6.89 ms                                                               | 8.59 ms: 1.25x slower                                                   |
| coverage                 | 83.6 ms                                                               | 105 ms: 1.25x slower                                                    |
| python_startup           | 11.2 ms                                                               | 15.0 ms: 1.34x slower                                                   |
| gc_traversal             | 4.15 ms                                                               | 7.17 ms: 1.72x slower                                                   |
| create_gc_cycles         | 2.26 ms                                                               | 4.13 ms: 1.83x slower                                                   |
| telco                    | 8.49 ms                                                               | 166 ms: 19.56x slower                                                   |
| bench_mp_pool            | 14.5 ms                                                               | 2.81 sec: 193.18x slower                                                |
| Geometric mean           | (ref)                                                                 | 1.20x faster                                                            |

Benchmark hidden because not significant (1): async_generators
Ignored benchmarks (13) of results/bm-20220323-3.10.4-9d38120/bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (17) of results/bm-20250712-3.15.0a0-47b01da/bm-20250712-arminc-aarch64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, djangocms, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, unpack_sequence

- Geometric mean (including insignificant results): 1.305x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.29x
- 95% likely to have a speedup of 1.27x
- 99% likely to have a speedup of 1.24x

# Memory
- memory change: 1.38x