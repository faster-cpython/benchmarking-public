# Results vs. 3.10.4

- fork: brandtbucher
- ref: justin_dwarf
- machine: linux-x86_64
- commit hash: 1ce520b
- commit date: 2024-11-15
- overall geometric mean: 1.396x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.25x faster
- Memory change: 1.41x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241115-linux-x86_64-brandtbucher-justin_dwarf-3.14.0a1+-1ce520b |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 276 ms: 1.26x faster                                                 |
| docutils       | 3.30 sec                                               | 3.00 sec: 1.10x faster                                               |
| html5lib       | 88.9 ms                                                | 66.4 ms: 1.34x faster                                                |
| Geometric mean | (ref)                                                  | 1.23x faster                                                         |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241115-linux-x86_64-brandtbucher-justin_dwarf-3.14.0a1+-1ce520b |
|-------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| async_tree_none         | 728 ms                                                 | 330 ms: 2.21x faster                                                 |
| async_tree_memoization  | 870 ms                                                 | 413 ms: 2.11x faster                                                 |
| async_tree_io           | 1.77 sec                                               | 854 ms: 2.07x faster                                                 |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 572 ms: 1.78x faster                                                 |
| Geometric mean          | (ref)                                                  | 2.03x faster                                                         |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241115-linux-x86_64-brandtbucher-justin_dwarf-3.14.0a1+-1ce520b |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 83.5 ms: 1.84x faster                                                |
| float          | 117 ms                                                 | 76.4 ms: 1.53x faster                                                |
| pidigits       | 191 ms                                                 | 187 ms: 1.02x faster                                                 |
| Geometric mean | (ref)                                                  | 1.42x faster                                                         |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241115-linux-x86_64-brandtbucher-justin_dwarf-3.14.0a1+-1ce520b |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 138 ms: 1.36x faster                                                 |
| regex_v8       | 27.8 ms                                                | 24.5 ms: 1.13x faster                                                |
| regex_dna      | 227 ms                                                 | 216 ms: 1.05x faster                                                 |
| regex_effbot   | 3.63 ms                                                | 3.79 ms: 1.04x slower                                                |
| Geometric mean | (ref)                                                  | 1.12x faster                                                         |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241115-linux-x86_64-brandtbucher-justin_dwarf-3.14.0a1+-1ce520b |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| tomli_loads          | 3.14 sec                                               | 1.93 sec: 1.63x faster                                               |
| unpickle_pure_python | 331 us                                                 | 217 us: 1.52x faster                                                 |
| pickle_pure_python   | 484 us                                                 | 321 us: 1.51x faster                                                 |
| xml_etree_process    | 79.1 ms                                                | 54.5 ms: 1.45x faster                                                |
| json_dumps           | 14.2 ms                                                | 10.7 ms: 1.32x faster                                                |
| xml_etree_generate   | 99.4 ms                                                | 78.6 ms: 1.27x faster                                                |
| json_loads           | 31.2 us                                                | 26.9 us: 1.16x faster                                                |
| xml_etree_iterparse  | 115 ms                                                 | 99.9 ms: 1.16x faster                                                |
| xml_etree_parse      | 168 ms                                                 | 147 ms: 1.14x faster                                                 |
| Geometric mean       | (ref)                                                  | 1.34x faster                                                         |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241115-linux-x86_64-brandtbucher-justin_dwarf-3.14.0a1+-1ce520b |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 12.8 ms: 1.14x faster                                                |
| python_startup_no_site | 5.93 ms                                                | 7.11 ms: 1.20x slower                                                |
| Geometric mean         | (ref)                                                  | 1.03x slower                                                         |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241115-linux-x86_64-brandtbucher-justin_dwarf-3.14.0a1+-1ce520b |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| mako            | 16.3 ms                                                | 10.3 ms: 1.58x faster                                                |
| django_template | 48.2 ms                                                | 33.4 ms: 1.44x faster                                                |
| genshi_text     | 31.8 ms                                                | 26.3 ms: 1.21x faster                                                |
| genshi_xml      | 66.0 ms                                                | 59.7 ms: 1.11x faster                                                |
| Geometric mean  | (ref)                                                  | 1.32x faster                                                         |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241115-linux-x86_64-brandtbucher-justin_dwarf-3.14.0a1+-1ce520b |
|--------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 167 us: 3.27x faster                                                 |
| deltablue                | 7.91 ms                                                | 3.27 ms: 2.42x faster                                                |
| generators               | 80.1 ms                                                | 34.3 ms: 2.34x faster                                                |
| async_tree_none          | 728 ms                                                 | 330 ms: 2.21x faster                                                 |
| async_tree_memoization   | 870 ms                                                 | 413 ms: 2.11x faster                                                 |
| async_tree_io            | 1.77 sec                                               | 854 ms: 2.07x faster                                                 |
| richards_super           | 94.7 ms                                                | 45.8 ms: 2.07x faster                                                |
| richards                 | 79.3 ms                                                | 38.9 ms: 2.04x faster                                                |
| deepcopy_memo            | 58.5 us                                                | 29.2 us: 2.00x faster                                                |
| chaos                    | 115 ms                                                 | 58.6 ms: 1.97x faster                                                |
| logging_silent           | 190 ns                                                 | 101 ns: 1.89x faster                                                 |
| scimark_sor              | 220 ms                                                 | 118 ms: 1.86x faster                                                 |
| go                       | 240 ms                                                 | 129 ms: 1.86x faster                                                 |
| crypto_pyaes             | 128 ms                                                 | 68.9 ms: 1.85x faster                                                |
| scimark_monte_carlo      | 118 ms                                                 | 63.9 ms: 1.85x faster                                                |
| raytrace                 | 507 ms                                                 | 275 ms: 1.84x faster                                                 |
| nbody                    | 154 ms                                                 | 83.5 ms: 1.84x faster                                                |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 572 ms: 1.78x faster                                                 |
| deepcopy                 | 479 us                                                 | 271 us: 1.77x faster                                                 |
| comprehensions           | 28.8 us                                                | 17.0 us: 1.69x faster                                                |
| sqlglot_parse            | 2.17 ms                                                | 1.32 ms: 1.65x faster                                                |
| tomli_loads              | 3.14 sec                                               | 1.93 sec: 1.63x faster                                               |
| pyflate                  | 716 ms                                                 | 448 ms: 1.60x faster                                                 |
| djangocms                | 38.4 us                                                | 24.0 us: 1.60x faster                                                |
| mako                     | 16.3 ms                                                | 10.3 ms: 1.58x faster                                                |
| scimark_lu               | 176 ms                                                 | 111 ms: 1.58x faster                                                 |
| coroutines               | 35.1 ms                                                | 22.5 ms: 1.56x faster                                                |
| sqlglot_transpile        | 2.57 ms                                                | 1.68 ms: 1.53x faster                                                |
| float                    | 117 ms                                                 | 76.4 ms: 1.53x faster                                                |
| deepcopy_reduce          | 4.17 us                                                | 2.74 us: 1.52x faster                                                |
| unpickle_pure_python     | 331 us                                                 | 217 us: 1.52x faster                                                 |
| pickle_pure_python       | 484 us                                                 | 321 us: 1.51x faster                                                 |
| hexiom                   | 10.4 ms                                                | 6.98 ms: 1.49x faster                                                |
| logging_simple           | 8.30 us                                                | 5.63 us: 1.48x faster                                                |
| spectral_norm            | 170 ms                                                 | 115 ms: 1.47x faster                                                 |
| pylint                   | 551 ms                                                 | 376 ms: 1.47x faster                                                 |
| logging_format           | 9.09 us                                                | 6.21 us: 1.46x faster                                                |
| xml_etree_process        | 79.1 ms                                                | 54.5 ms: 1.45x faster                                                |
| django_template          | 48.2 ms                                                | 33.4 ms: 1.44x faster                                                |
| scimark_fft              | 466 ms                                                 | 326 ms: 1.43x faster                                                 |
| pprint_safe_repr         | 1.02 sec                                               | 713 ms: 1.43x faster                                                 |
| pprint_pformat           | 2.10 sec                                               | 1.48 sec: 1.42x faster                                               |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.57 ms: 1.42x faster                                                |
| fannkuch                 | 532 ms                                                 | 377 ms: 1.41x faster                                                 |
| regex_compile            | 188 ms                                                 | 138 ms: 1.36x faster                                                 |
| thrift                   | 1.07 ms                                                | 787 us: 1.36x faster                                                 |
| pycparser                | 1.58 sec                                               | 1.16 sec: 1.36x faster                                               |
| html5lib                 | 88.9 ms                                                | 66.4 ms: 1.34x faster                                                |
| json_dumps               | 14.2 ms                                                | 10.7 ms: 1.32x faster                                                |
| sqlalchemy_imperative    | 23.3 ms                                                | 17.8 ms: 1.31x faster                                                |
| sqlglot_normalize        | 143 ms                                                 | 112 ms: 1.28x faster                                                 |
| pathlib                  | 20.5 ms                                                | 16.1 ms: 1.27x faster                                                |
| xml_etree_generate       | 99.4 ms                                                | 78.6 ms: 1.27x faster                                                |
| 2to3                     | 348 ms                                                 | 276 ms: 1.26x faster                                                 |
| dulwich_log              | 84.3 ms                                                | 68.0 ms: 1.24x faster                                                |
| genshi_text              | 31.8 ms                                                | 26.3 ms: 1.21x faster                                                |
| sqlglot_optimize         | 69.2 ms                                                | 57.4 ms: 1.21x faster                                                |
| nqueens                  | 106 ms                                                 | 89.3 ms: 1.19x faster                                                |
| sqlalchemy_declarative   | 172 ms                                                 | 147 ms: 1.17x faster                                                 |
| json_loads               | 31.2 us                                                | 26.9 us: 1.16x faster                                                |
| xml_etree_iterparse      | 115 ms                                                 | 99.9 ms: 1.16x faster                                                |
| sympy_str                | 346 ms                                                 | 302 ms: 1.15x faster                                                 |
| json                     | 5.69 ms                                                | 4.97 ms: 1.15x faster                                                |
| xml_etree_parse          | 168 ms                                                 | 147 ms: 1.14x faster                                                 |
| python_startup           | 14.6 ms                                                | 12.8 ms: 1.14x faster                                                |
| sympy_sum                | 196 ms                                                 | 173 ms: 1.14x faster                                                 |
| regex_v8                 | 27.8 ms                                                | 24.5 ms: 1.13x faster                                                |
| meteor_contest           | 120 ms                                                 | 107 ms: 1.12x faster                                                 |
| bench_thread_pool        | 986 us                                                 | 886 us: 1.11x faster                                                 |
| sympy_expand             | 566 ms                                                 | 508 ms: 1.11x faster                                                 |
| sympy_integrate          | 25.8 ms                                                | 23.2 ms: 1.11x faster                                                |
| genshi_xml               | 66.0 ms                                                | 59.7 ms: 1.11x faster                                                |
| docutils                 | 3.30 sec                                               | 3.00 sec: 1.10x faster                                               |
| sqlite_synth             | 3.02 us                                                | 2.76 us: 1.09x faster                                                |
| regex_dna                | 227 ms                                                 | 216 ms: 1.05x faster                                                 |
| mdp                      | 2.85 sec                                               | 2.73 sec: 1.04x faster                                               |
| pidigits                 | 191 ms                                                 | 187 ms: 1.02x faster                                                 |
| asyncio_websockets       | 559 ms                                                 | 553 ms: 1.01x faster                                                 |
| async_generators         | 444 ms                                                 | 454 ms: 1.02x slower                                                 |
| regex_effbot             | 3.63 ms                                                | 3.79 ms: 1.04x slower                                                |
| telco                    | 7.27 ms                                                | 7.61 ms: 1.05x slower                                                |
| coverage                 | 79.4 ms                                                | 83.7 ms: 1.05x slower                                                |
| python_startup_no_site   | 5.93 ms                                                | 7.11 ms: 1.20x slower                                                |
| gc_traversal             | 3.62 ms                                                | 4.36 ms: 1.20x slower                                                |
| create_gc_cycles         | 1.62 ms                                                | 2.70 ms: 1.67x slower                                                |
| bench_mp_pool            | 24.0 ms                                                | 85.2 ms: 3.55x slower                                                |
| Geometric mean           | (ref)                                                  | 1.37x faster                                                         |
Ignored benchmarks (15) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (11) of results/bm-20241115-3.14.0a1+-1ce520b-JIT/bm-20241115-linux-x86_64-brandtbucher-justin_dwarf-3.14.0a1+-1ce520b.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.396x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.32x
- 95% likely to have a speedup of 1.28x
- 99% likely to have a speedup of 1.25x

# Memory
- memory change: 1.41x