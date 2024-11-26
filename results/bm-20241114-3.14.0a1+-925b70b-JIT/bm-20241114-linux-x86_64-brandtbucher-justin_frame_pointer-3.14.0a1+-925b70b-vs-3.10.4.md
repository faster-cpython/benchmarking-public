# Results vs. 3.10.4

- fork: brandtbucher
- ref: justin_frame_pointer
- machine: linux-x86_64
- commit hash: 925b70b
- commit date: 2024-11-14
- overall geometric mean: 1.348x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.21x faster
- Memory change: 1.34x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241114-linux-x86_64-brandtbucher-justin_frame_pointer-3.14.0a1+-925b70b |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 286 ms: 1.22x faster                                                         |
| docutils       | 3.30 sec                                               | 2.97 sec: 1.11x faster                                                       |
| html5lib       | 88.9 ms                                                | 67.9 ms: 1.31x faster                                                        |
| Geometric mean | (ref)                                                  | 1.21x faster                                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241114-linux-x86_64-brandtbucher-justin_frame_pointer-3.14.0a1+-925b70b |
|-------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_none         | 728 ms                                                 | 337 ms: 2.16x faster                                                         |
| async_tree_memoization  | 870 ms                                                 | 425 ms: 2.05x faster                                                         |
| async_tree_io           | 1.77 sec                                               | 876 ms: 2.02x faster                                                         |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 577 ms: 1.76x faster                                                         |
| Geometric mean          | (ref)                                                  | 1.99x faster                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241114-linux-x86_64-brandtbucher-justin_frame_pointer-3.14.0a1+-925b70b |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 90.0 ms: 1.71x faster                                                        |
| float          | 117 ms                                                 | 79.1 ms: 1.48x faster                                                        |
| pidigits       | 191 ms                                                 | 187 ms: 1.02x faster                                                         |
| Geometric mean | (ref)                                                  | 1.37x faster                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241114-linux-x86_64-brandtbucher-justin_frame_pointer-3.14.0a1+-925b70b |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 144 ms: 1.31x faster                                                         |
| regex_v8       | 27.8 ms                                                | 24.8 ms: 1.12x faster                                                        |
| regex_dna      | 227 ms                                                 | 217 ms: 1.05x faster                                                         |
| regex_effbot   | 3.63 ms                                                | 3.72 ms: 1.03x slower                                                        |
| Geometric mean | (ref)                                                  | 1.11x faster                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241114-linux-x86_64-brandtbucher-justin_frame_pointer-3.14.0a1+-925b70b |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| tomli_loads          | 3.14 sec                                               | 2.05 sec: 1.54x faster                                                       |
| unpickle_pure_python | 331 us                                                 | 223 us: 1.48x faster                                                         |
| pickle_pure_python   | 484 us                                                 | 332 us: 1.46x faster                                                         |
| xml_etree_process    | 79.1 ms                                                | 57.8 ms: 1.37x faster                                                        |
| json_dumps           | 14.2 ms                                                | 11.1 ms: 1.27x faster                                                        |
| xml_etree_generate   | 99.4 ms                                                | 82.5 ms: 1.20x faster                                                        |
| json_loads           | 31.2 us                                                | 27.0 us: 1.16x faster                                                        |
| xml_etree_iterparse  | 115 ms                                                 | 102 ms: 1.13x faster                                                         |
| xml_etree_parse      | 168 ms                                                 | 149 ms: 1.13x faster                                                         |
| Geometric mean       | (ref)                                                  | 1.30x faster                                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241114-linux-x86_64-brandtbucher-justin_frame_pointer-3.14.0a1+-925b70b |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 12.8 ms: 1.14x faster                                                        |
| python_startup_no_site | 5.93 ms                                                | 7.11 ms: 1.20x slower                                                        |
| Geometric mean         | (ref)                                                  | 1.03x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241114-linux-x86_64-brandtbucher-justin_frame_pointer-3.14.0a1+-925b70b |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| mako            | 16.3 ms                                                | 10.8 ms: 1.51x faster                                                        |
| django_template | 48.2 ms                                                | 34.6 ms: 1.39x faster                                                        |
| genshi_text     | 31.8 ms                                                | 27.2 ms: 1.17x faster                                                        |
| genshi_xml      | 66.0 ms                                                | 62.0 ms: 1.07x faster                                                        |
| Geometric mean  | (ref)                                                  | 1.27x faster                                                                 |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241114-linux-x86_64-brandtbucher-justin_frame_pointer-3.14.0a1+-925b70b |
|--------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 175 us: 3.11x faster                                                         |
| deltablue                | 7.91 ms                                                | 3.57 ms: 2.22x faster                                                        |
| async_tree_none          | 728 ms                                                 | 337 ms: 2.16x faster                                                         |
| async_tree_memoization   | 870 ms                                                 | 425 ms: 2.05x faster                                                         |
| async_tree_io            | 1.77 sec                                               | 876 ms: 2.02x faster                                                         |
| richards_super           | 94.7 ms                                                | 47.9 ms: 1.98x faster                                                        |
| generators               | 80.1 ms                                                | 41.9 ms: 1.91x faster                                                        |
| chaos                    | 115 ms                                                 | 61.9 ms: 1.87x faster                                                        |
| richards                 | 79.3 ms                                                | 43.2 ms: 1.83x faster                                                        |
| deepcopy_memo            | 58.5 us                                                | 32.0 us: 1.83x faster                                                        |
| crypto_pyaes             | 128 ms                                                 | 72.3 ms: 1.77x faster                                                        |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 577 ms: 1.76x faster                                                         |
| scimark_monte_carlo      | 118 ms                                                 | 67.2 ms: 1.76x faster                                                        |
| raytrace                 | 507 ms                                                 | 288 ms: 1.76x faster                                                         |
| logging_silent           | 190 ns                                                 | 108 ns: 1.76x faster                                                         |
| scimark_sor              | 220 ms                                                 | 126 ms: 1.75x faster                                                         |
| go                       | 240 ms                                                 | 139 ms: 1.72x faster                                                         |
| nbody                    | 154 ms                                                 | 90.0 ms: 1.71x faster                                                        |
| deepcopy                 | 479 us                                                 | 281 us: 1.70x faster                                                         |
| djangocms                | 38.4 us                                                | 23.3 us: 1.65x faster                                                        |
| sqlglot_parse            | 2.17 ms                                                | 1.36 ms: 1.60x faster                                                        |
| coroutines               | 35.1 ms                                                | 22.8 ms: 1.54x faster                                                        |
| tomli_loads              | 3.14 sec                                               | 2.05 sec: 1.54x faster                                                       |
| comprehensions           | 28.8 us                                                | 18.8 us: 1.53x faster                                                        |
| mako                     | 16.3 ms                                                | 10.8 ms: 1.51x faster                                                        |
| deepcopy_reduce          | 4.17 us                                                | 2.79 us: 1.49x faster                                                        |
| sqlglot_transpile        | 2.57 ms                                                | 1.73 ms: 1.49x faster                                                        |
| logging_format           | 9.09 us                                                | 6.11 us: 1.49x faster                                                        |
| pyflate                  | 716 ms                                                 | 482 ms: 1.49x faster                                                         |
| logging_simple           | 8.30 us                                                | 5.60 us: 1.48x faster                                                        |
| float                    | 117 ms                                                 | 79.1 ms: 1.48x faster                                                        |
| unpickle_pure_python     | 331 us                                                 | 223 us: 1.48x faster                                                         |
| scimark_lu               | 176 ms                                                 | 119 ms: 1.48x faster                                                         |
| pickle_pure_python       | 484 us                                                 | 332 us: 1.46x faster                                                         |
| pylint                   | 551 ms                                                 | 380 ms: 1.45x faster                                                         |
| django_template          | 48.2 ms                                                | 34.6 ms: 1.39x faster                                                        |
| spectral_norm            | 170 ms                                                 | 122 ms: 1.39x faster                                                         |
| scimark_fft              | 466 ms                                                 | 337 ms: 1.38x faster                                                         |
| hexiom                   | 10.4 ms                                                | 7.57 ms: 1.37x faster                                                        |
| xml_etree_process        | 79.1 ms                                                | 57.8 ms: 1.37x faster                                                        |
| thrift                   | 1.07 ms                                                | 785 us: 1.36x faster                                                         |
| pprint_pformat           | 2.10 sec                                               | 1.54 sec: 1.36x faster                                                       |
| pycparser                | 1.58 sec                                               | 1.17 sec: 1.35x faster                                                       |
| pprint_safe_repr         | 1.02 sec                                               | 760 ms: 1.34x faster                                                         |
| sqlalchemy_imperative    | 23.3 ms                                                | 17.7 ms: 1.32x faster                                                        |
| fannkuch                 | 532 ms                                                 | 405 ms: 1.31x faster                                                         |
| regex_compile            | 188 ms                                                 | 144 ms: 1.31x faster                                                         |
| html5lib                 | 88.9 ms                                                | 67.9 ms: 1.31x faster                                                        |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.97 ms: 1.30x faster                                                        |
| json_dumps               | 14.2 ms                                                | 11.1 ms: 1.27x faster                                                        |
| pathlib                  | 20.5 ms                                                | 16.4 ms: 1.25x faster                                                        |
| dulwich_log              | 84.3 ms                                                | 68.1 ms: 1.24x faster                                                        |
| 2to3                     | 348 ms                                                 | 286 ms: 1.22x faster                                                         |
| sqlglot_normalize        | 143 ms                                                 | 118 ms: 1.21x faster                                                         |
| xml_etree_generate       | 99.4 ms                                                | 82.5 ms: 1.20x faster                                                        |
| genshi_text              | 31.8 ms                                                | 27.2 ms: 1.17x faster                                                        |
| json_loads               | 31.2 us                                                | 27.0 us: 1.16x faster                                                        |
| sqlalchemy_declarative   | 172 ms                                                 | 149 ms: 1.15x faster                                                         |
| nqueens                  | 106 ms                                                 | 92.2 ms: 1.15x faster                                                        |
| python_startup           | 14.6 ms                                                | 12.8 ms: 1.14x faster                                                        |
| json                     | 5.69 ms                                                | 5.02 ms: 1.13x faster                                                        |
| xml_etree_iterparse      | 115 ms                                                 | 102 ms: 1.13x faster                                                         |
| xml_etree_parse          | 168 ms                                                 | 149 ms: 1.13x faster                                                         |
| sympy_str                | 346 ms                                                 | 307 ms: 1.13x faster                                                         |
| regex_v8                 | 27.8 ms                                                | 24.8 ms: 1.12x faster                                                        |
| sqlglot_optimize         | 69.2 ms                                                | 61.7 ms: 1.12x faster                                                        |
| sympy_expand             | 566 ms                                                 | 510 ms: 1.11x faster                                                         |
| docutils                 | 3.30 sec                                               | 2.97 sec: 1.11x faster                                                       |
| sympy_sum                | 196 ms                                                 | 178 ms: 1.11x faster                                                         |
| bench_thread_pool        | 986 us                                                 | 908 us: 1.09x faster                                                         |
| sympy_integrate          | 25.8 ms                                                | 23.9 ms: 1.08x faster                                                        |
| sqlite_synth             | 3.02 us                                                | 2.83 us: 1.07x faster                                                        |
| genshi_xml               | 66.0 ms                                                | 62.0 ms: 1.07x faster                                                        |
| meteor_contest           | 120 ms                                                 | 112 ms: 1.06x faster                                                         |
| regex_dna                | 227 ms                                                 | 217 ms: 1.05x faster                                                         |
| mdp                      | 2.85 sec                                               | 2.75 sec: 1.04x faster                                                       |
| pidigits                 | 191 ms                                                 | 187 ms: 1.02x faster                                                         |
| asyncio_websockets       | 559 ms                                                 | 553 ms: 1.01x faster                                                         |
| async_generators         | 444 ms                                                 | 455 ms: 1.02x slower                                                         |
| regex_effbot             | 3.63 ms                                                | 3.72 ms: 1.03x slower                                                        |
| coverage                 | 79.4 ms                                                | 84.9 ms: 1.07x slower                                                        |
| telco                    | 7.27 ms                                                | 7.83 ms: 1.08x slower                                                        |
| python_startup_no_site   | 5.93 ms                                                | 7.11 ms: 1.20x slower                                                        |
| gc_traversal             | 3.62 ms                                                | 4.64 ms: 1.28x slower                                                        |
| create_gc_cycles         | 1.62 ms                                                | 2.70 ms: 1.66x slower                                                        |
| bench_mp_pool            | 24.0 ms                                                | 84.6 ms: 3.52x slower                                                        |
| Geometric mean           | (ref)                                                  | 1.32x faster                                                                 |
Ignored benchmarks (15) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (9) of results/bm-20241114-3.14.0a1+-925b70b-JIT/bm-20241114-linux-x86_64-brandtbucher-justin_frame_pointer-3.14.0a1+-925b70b.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, shortest_path, sphinx

- Geometric mean (including insignificant results): 1.348x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.27x
- 95% likely to have a speedup of 1.24x
- 99% likely to have a speedup of 1.21x

# Memory
- memory change: 1.34x