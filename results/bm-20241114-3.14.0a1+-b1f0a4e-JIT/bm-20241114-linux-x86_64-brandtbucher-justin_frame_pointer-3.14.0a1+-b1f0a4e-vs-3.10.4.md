# Results vs. 3.10.4

- fork: brandtbucher
- ref: justin_frame_pointer
- machine: linux-x86_64
- commit hash: b1f0a4e
- commit date: 2024-11-14
- overall geometric mean: 1.350x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.21x faster
- Memory change: 1.34x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241114-linux-x86_64-brandtbucher-justin_frame_pointer-3.14.0a1+-b1f0a4e |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 286 ms: 1.22x faster                                                         |
| docutils       | 3.30 sec                                               | 2.96 sec: 1.11x faster                                                       |
| html5lib       | 88.9 ms                                                | 66.6 ms: 1.33x faster                                                        |
| Geometric mean | (ref)                                                  | 1.22x faster                                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241114-linux-x86_64-brandtbucher-justin_frame_pointer-3.14.0a1+-b1f0a4e |
|-------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_none         | 728 ms                                                 | 335 ms: 2.17x faster                                                         |
| async_tree_memoization  | 870 ms                                                 | 424 ms: 2.05x faster                                                         |
| async_tree_io           | 1.77 sec                                               | 867 ms: 2.04x faster                                                         |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 585 ms: 1.74x faster                                                         |
| Geometric mean          | (ref)                                                  | 1.99x faster                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241114-linux-x86_64-brandtbucher-justin_frame_pointer-3.14.0a1+-b1f0a4e |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 91.0 ms: 1.69x faster                                                        |
| float          | 117 ms                                                 | 79.2 ms: 1.48x faster                                                        |
| pidigits       | 191 ms                                                 | 187 ms: 1.02x faster                                                         |
| Geometric mean | (ref)                                                  | 1.37x faster                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241114-linux-x86_64-brandtbucher-justin_frame_pointer-3.14.0a1+-b1f0a4e |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 143 ms: 1.32x faster                                                         |
| regex_v8       | 27.8 ms                                                | 24.8 ms: 1.12x faster                                                        |
| regex_dna      | 227 ms                                                 | 215 ms: 1.06x faster                                                         |
| regex_effbot   | 3.63 ms                                                | 3.77 ms: 1.04x slower                                                        |
| Geometric mean | (ref)                                                  | 1.11x faster                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241114-linux-x86_64-brandtbucher-justin_frame_pointer-3.14.0a1+-b1f0a4e |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| tomli_loads          | 3.14 sec                                               | 2.08 sec: 1.51x faster                                                       |
| unpickle_pure_python | 331 us                                                 | 224 us: 1.47x faster                                                         |
| pickle_pure_python   | 484 us                                                 | 329 us: 1.47x faster                                                         |
| xml_etree_process    | 79.1 ms                                                | 58.1 ms: 1.36x faster                                                        |
| json_dumps           | 14.2 ms                                                | 11.3 ms: 1.26x faster                                                        |
| xml_etree_generate   | 99.4 ms                                                | 82.8 ms: 1.20x faster                                                        |
| json_loads           | 31.2 us                                                | 26.8 us: 1.16x faster                                                        |
| xml_etree_parse      | 168 ms                                                 | 149 ms: 1.13x faster                                                         |
| xml_etree_iterparse  | 115 ms                                                 | 102 ms: 1.13x faster                                                         |
| Geometric mean       | (ref)                                                  | 1.29x faster                                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241114-linux-x86_64-brandtbucher-justin_frame_pointer-3.14.0a1+-b1f0a4e |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 12.8 ms: 1.14x faster                                                        |
| python_startup_no_site | 5.93 ms                                                | 7.11 ms: 1.20x slower                                                        |
| Geometric mean         | (ref)                                                  | 1.03x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241114-linux-x86_64-brandtbucher-justin_frame_pointer-3.14.0a1+-b1f0a4e |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| mako            | 16.3 ms                                                | 10.9 ms: 1.50x faster                                                        |
| django_template | 48.2 ms                                                | 34.6 ms: 1.39x faster                                                        |
| genshi_text     | 31.8 ms                                                | 25.6 ms: 1.24x faster                                                        |
| genshi_xml      | 66.0 ms                                                | 59.8 ms: 1.10x faster                                                        |
| Geometric mean  | (ref)                                                  | 1.30x faster                                                                 |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241114-linux-x86_64-brandtbucher-justin_frame_pointer-3.14.0a1+-b1f0a4e |
|--------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 171 us: 3.18x faster                                                         |
| deltablue                | 7.91 ms                                                | 3.61 ms: 2.19x faster                                                        |
| async_tree_none          | 728 ms                                                 | 335 ms: 2.17x faster                                                         |
| async_tree_memoization   | 870 ms                                                 | 424 ms: 2.05x faster                                                         |
| async_tree_io            | 1.77 sec                                               | 867 ms: 2.04x faster                                                         |
| generators               | 80.1 ms                                                | 39.7 ms: 2.02x faster                                                        |
| richards_super           | 94.7 ms                                                | 48.0 ms: 1.97x faster                                                        |
| chaos                    | 115 ms                                                 | 61.7 ms: 1.87x faster                                                        |
| deepcopy_memo            | 58.5 us                                                | 31.8 us: 1.84x faster                                                        |
| richards                 | 79.3 ms                                                | 43.2 ms: 1.84x faster                                                        |
| crypto_pyaes             | 128 ms                                                 | 72.2 ms: 1.77x faster                                                        |
| raytrace                 | 507 ms                                                 | 287 ms: 1.77x faster                                                         |
| scimark_sor              | 220 ms                                                 | 125 ms: 1.75x faster                                                         |
| logging_silent           | 190 ns                                                 | 109 ns: 1.74x faster                                                         |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 585 ms: 1.74x faster                                                         |
| scimark_monte_carlo      | 118 ms                                                 | 68.1 ms: 1.74x faster                                                        |
| deepcopy                 | 479 us                                                 | 278 us: 1.72x faster                                                         |
| go                       | 240 ms                                                 | 140 ms: 1.72x faster                                                         |
| nbody                    | 154 ms                                                 | 91.0 ms: 1.69x faster                                                        |
| sqlglot_parse            | 2.17 ms                                                | 1.35 ms: 1.61x faster                                                        |
| djangocms                | 38.4 us                                                | 24.0 us: 1.60x faster                                                        |
| coroutines               | 35.1 ms                                                | 22.9 ms: 1.53x faster                                                        |
| comprehensions           | 28.8 us                                                | 18.8 us: 1.53x faster                                                        |
| tomli_loads              | 3.14 sec                                               | 2.08 sec: 1.51x faster                                                       |
| mako                     | 16.3 ms                                                | 10.9 ms: 1.50x faster                                                        |
| deepcopy_reduce          | 4.17 us                                                | 2.78 us: 1.50x faster                                                        |
| scimark_lu               | 176 ms                                                 | 118 ms: 1.49x faster                                                         |
| sqlglot_transpile        | 2.57 ms                                                | 1.73 ms: 1.49x faster                                                        |
| float                    | 117 ms                                                 | 79.2 ms: 1.48x faster                                                        |
| unpickle_pure_python     | 331 us                                                 | 224 us: 1.47x faster                                                         |
| pyflate                  | 716 ms                                                 | 487 ms: 1.47x faster                                                         |
| pickle_pure_python       | 484 us                                                 | 329 us: 1.47x faster                                                         |
| logging_format           | 9.09 us                                                | 6.26 us: 1.45x faster                                                        |
| pylint                   | 551 ms                                                 | 381 ms: 1.45x faster                                                         |
| logging_simple           | 8.30 us                                                | 5.78 us: 1.44x faster                                                        |
| django_template          | 48.2 ms                                                | 34.6 ms: 1.39x faster                                                        |
| hexiom                   | 10.4 ms                                                | 7.53 ms: 1.38x faster                                                        |
| spectral_norm            | 170 ms                                                 | 123 ms: 1.38x faster                                                         |
| thrift                   | 1.07 ms                                                | 787 us: 1.36x faster                                                         |
| xml_etree_process        | 79.1 ms                                                | 58.1 ms: 1.36x faster                                                        |
| scimark_fft              | 466 ms                                                 | 343 ms: 1.36x faster                                                         |
| pycparser                | 1.58 sec                                               | 1.16 sec: 1.36x faster                                                       |
| pprint_safe_repr         | 1.02 sec                                               | 756 ms: 1.35x faster                                                         |
| html5lib                 | 88.9 ms                                                | 66.6 ms: 1.33x faster                                                        |
| pprint_pformat           | 2.10 sec                                               | 1.59 sec: 1.32x faster                                                       |
| regex_compile            | 188 ms                                                 | 143 ms: 1.32x faster                                                         |
| sqlalchemy_imperative    | 23.3 ms                                                | 17.9 ms: 1.31x faster                                                        |
| fannkuch                 | 532 ms                                                 | 407 ms: 1.31x faster                                                         |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 5.01 ms: 1.29x faster                                                        |
| pathlib                  | 20.5 ms                                                | 16.2 ms: 1.27x faster                                                        |
| json_dumps               | 14.2 ms                                                | 11.3 ms: 1.26x faster                                                        |
| genshi_text              | 31.8 ms                                                | 25.6 ms: 1.24x faster                                                        |
| dulwich_log              | 84.3 ms                                                | 69.1 ms: 1.22x faster                                                        |
| 2to3                     | 348 ms                                                 | 286 ms: 1.22x faster                                                         |
| sqlglot_normalize        | 143 ms                                                 | 118 ms: 1.22x faster                                                         |
| xml_etree_generate       | 99.4 ms                                                | 82.8 ms: 1.20x faster                                                        |
| json_loads               | 31.2 us                                                | 26.8 us: 1.16x faster                                                        |
| sqlalchemy_declarative   | 172 ms                                                 | 149 ms: 1.16x faster                                                         |
| nqueens                  | 106 ms                                                 | 91.5 ms: 1.16x faster                                                        |
| python_startup           | 14.6 ms                                                | 12.8 ms: 1.14x faster                                                        |
| json                     | 5.69 ms                                                | 5.01 ms: 1.14x faster                                                        |
| sqlglot_optimize         | 69.2 ms                                                | 61.3 ms: 1.13x faster                                                        |
| xml_etree_parse          | 168 ms                                                 | 149 ms: 1.13x faster                                                         |
| sympy_str                | 346 ms                                                 | 307 ms: 1.13x faster                                                         |
| xml_etree_iterparse      | 115 ms                                                 | 102 ms: 1.13x faster                                                         |
| regex_v8                 | 27.8 ms                                                | 24.8 ms: 1.12x faster                                                        |
| sympy_expand             | 566 ms                                                 | 508 ms: 1.11x faster                                                         |
| docutils                 | 3.30 sec                                               | 2.96 sec: 1.11x faster                                                       |
| genshi_xml               | 66.0 ms                                                | 59.8 ms: 1.10x faster                                                        |
| sympy_sum                | 196 ms                                                 | 178 ms: 1.10x faster                                                         |
| mdp                      | 2.85 sec                                               | 2.61 sec: 1.09x faster                                                       |
| bench_thread_pool        | 986 us                                                 | 907 us: 1.09x faster                                                         |
| sympy_integrate          | 25.8 ms                                                | 23.8 ms: 1.08x faster                                                        |
| sqlite_synth             | 3.02 us                                                | 2.81 us: 1.08x faster                                                        |
| meteor_contest           | 120 ms                                                 | 112 ms: 1.07x faster                                                         |
| regex_dna                | 227 ms                                                 | 215 ms: 1.06x faster                                                         |
| pidigits                 | 191 ms                                                 | 187 ms: 1.02x faster                                                         |
| asyncio_websockets       | 559 ms                                                 | 552 ms: 1.01x faster                                                         |
| async_generators         | 444 ms                                                 | 460 ms: 1.04x slower                                                         |
| regex_effbot             | 3.63 ms                                                | 3.77 ms: 1.04x slower                                                        |
| coverage                 | 79.4 ms                                                | 84.4 ms: 1.06x slower                                                        |
| telco                    | 7.27 ms                                                | 7.85 ms: 1.08x slower                                                        |
| python_startup_no_site   | 5.93 ms                                                | 7.11 ms: 1.20x slower                                                        |
| gc_traversal             | 3.62 ms                                                | 4.52 ms: 1.25x slower                                                        |
| create_gc_cycles         | 1.62 ms                                                | 2.70 ms: 1.66x slower                                                        |
| bench_mp_pool            | 24.0 ms                                                | 84.8 ms: 3.53x slower                                                        |
| Geometric mean           | (ref)                                                  | 1.33x faster                                                                 |
Ignored benchmarks (15) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (11) of results/bm-20241114-3.14.0a1+-b1f0a4e-JIT/bm-20241114-linux-x86_64-brandtbucher-justin_frame_pointer-3.14.0a1+-b1f0a4e.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.350x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.27x
- 95% likely to have a speedup of 1.25x
- 99% likely to have a speedup of 1.21x

# Memory
- memory change: 1.34x