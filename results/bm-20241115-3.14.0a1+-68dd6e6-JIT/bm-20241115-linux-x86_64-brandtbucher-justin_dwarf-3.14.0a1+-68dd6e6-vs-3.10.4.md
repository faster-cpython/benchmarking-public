# Results vs. 3.10.4

- fork: brandtbucher
- ref: justin_dwarf
- machine: linux-x86_64
- commit hash: 68dd6e6
- commit date: 2024-11-15
- overall geometric mean: 1.389x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.23x faster
- Memory change: 1.37x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241115-linux-x86_64-brandtbucher-justin_dwarf-3.14.0a1+-68dd6e6 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 282 ms: 1.24x faster                                                 |
| docutils       | 3.30 sec                                               | 2.95 sec: 1.12x faster                                               |
| html5lib       | 88.9 ms                                                | 67.6 ms: 1.31x faster                                                |
| Geometric mean | (ref)                                                  | 1.22x faster                                                         |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241115-linux-x86_64-brandtbucher-justin_dwarf-3.14.0a1+-68dd6e6 |
|-------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| async_tree_none         | 728 ms                                                 | 329 ms: 2.21x faster                                                 |
| async_tree_memoization  | 870 ms                                                 | 415 ms: 2.10x faster                                                 |
| async_tree_io           | 1.77 sec                                               | 854 ms: 2.07x faster                                                 |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 566 ms: 1.79x faster                                                 |
| Geometric mean          | (ref)                                                  | 2.04x faster                                                         |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241115-linux-x86_64-brandtbucher-justin_dwarf-3.14.0a1+-68dd6e6 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 83.2 ms: 1.85x faster                                                |
| float          | 117 ms                                                 | 76.5 ms: 1.53x faster                                                |
| pidigits       | 191 ms                                                 | 186 ms: 1.02x faster                                                 |
| Geometric mean | (ref)                                                  | 1.42x faster                                                         |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241115-linux-x86_64-brandtbucher-justin_dwarf-3.14.0a1+-68dd6e6 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 141 ms: 1.34x faster                                                 |
| regex_v8       | 27.8 ms                                                | 25.3 ms: 1.10x faster                                                |
| regex_dna      | 227 ms                                                 | 210 ms: 1.08x faster                                                 |
| Geometric mean | (ref)                                                  | 1.13x faster                                                         |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241115-linux-x86_64-brandtbucher-justin_dwarf-3.14.0a1+-68dd6e6 |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| tomli_loads          | 3.14 sec                                               | 1.94 sec: 1.62x faster                                               |
| pickle_pure_python   | 484 us                                                 | 318 us: 1.52x faster                                                 |
| unpickle_pure_python | 331 us                                                 | 219 us: 1.51x faster                                                 |
| xml_etree_process    | 79.1 ms                                                | 56.0 ms: 1.41x faster                                                |
| json_dumps           | 14.2 ms                                                | 10.9 ms: 1.31x faster                                                |
| xml_etree_generate   | 99.4 ms                                                | 79.1 ms: 1.26x faster                                                |
| json_loads           | 31.2 us                                                | 26.5 us: 1.18x faster                                                |
| xml_etree_iterparse  | 115 ms                                                 | 101 ms: 1.15x faster                                                 |
| xml_etree_parse      | 168 ms                                                 | 148 ms: 1.13x faster                                                 |
| Geometric mean       | (ref)                                                  | 1.33x faster                                                         |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241115-linux-x86_64-brandtbucher-justin_dwarf-3.14.0a1+-68dd6e6 |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 12.8 ms: 1.14x faster                                                |
| python_startup_no_site | 5.93 ms                                                | 7.13 ms: 1.20x slower                                                |
| Geometric mean         | (ref)                                                  | 1.03x slower                                                         |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241115-linux-x86_64-brandtbucher-justin_dwarf-3.14.0a1+-68dd6e6 |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| mako            | 16.3 ms                                                | 10.1 ms: 1.61x faster                                                |
| django_template | 48.2 ms                                                | 33.7 ms: 1.43x faster                                                |
| genshi_text     | 31.8 ms                                                | 24.8 ms: 1.28x faster                                                |
| genshi_xml      | 66.0 ms                                                | 59.0 ms: 1.12x faster                                                |
| Geometric mean  | (ref)                                                  | 1.35x faster                                                         |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241115-linux-x86_64-brandtbucher-justin_dwarf-3.14.0a1+-68dd6e6 |
|--------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 166 us: 3.28x faster                                                 |
| deltablue                | 7.91 ms                                                | 3.28 ms: 2.41x faster                                                |
| generators               | 80.1 ms                                                | 35.9 ms: 2.23x faster                                                |
| async_tree_none          | 728 ms                                                 | 329 ms: 2.21x faster                                                 |
| richards_super           | 94.7 ms                                                | 44.9 ms: 2.11x faster                                                |
| async_tree_memoization   | 870 ms                                                 | 415 ms: 2.10x faster                                                 |
| async_tree_io            | 1.77 sec                                               | 854 ms: 2.07x faster                                                 |
| richards                 | 79.3 ms                                                | 39.8 ms: 1.99x faster                                                |
| deepcopy_memo            | 58.5 us                                                | 29.5 us: 1.98x faster                                                |
| chaos                    | 115 ms                                                 | 58.8 ms: 1.96x faster                                                |
| logging_silent           | 190 ns                                                 | 97.3 ns: 1.95x faster                                                |
| crypto_pyaes             | 128 ms                                                 | 68.8 ms: 1.86x faster                                                |
| raytrace                 | 507 ms                                                 | 274 ms: 1.85x faster                                                 |
| nbody                    | 154 ms                                                 | 83.2 ms: 1.85x faster                                                |
| scimark_monte_carlo      | 118 ms                                                 | 64.3 ms: 1.84x faster                                                |
| scimark_sor              | 220 ms                                                 | 120 ms: 1.83x faster                                                 |
| go                       | 240 ms                                                 | 133 ms: 1.81x faster                                                 |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 566 ms: 1.79x faster                                                 |
| deepcopy                 | 479 us                                                 | 268 us: 1.79x faster                                                 |
| comprehensions           | 28.8 us                                                | 17.6 us: 1.63x faster                                                |
| sqlglot_parse            | 2.17 ms                                                | 1.33 ms: 1.63x faster                                                |
| tomli_loads              | 3.14 sec                                               | 1.94 sec: 1.62x faster                                               |
| djangocms                | 38.4 us                                                | 23.8 us: 1.61x faster                                                |
| mako                     | 16.3 ms                                                | 10.1 ms: 1.61x faster                                                |
| pyflate                  | 716 ms                                                 | 455 ms: 1.58x faster                                                 |
| coroutines               | 35.1 ms                                                | 22.7 ms: 1.55x faster                                                |
| deepcopy_reduce          | 4.17 us                                                | 2.72 us: 1.54x faster                                                |
| scimark_lu               | 176 ms                                                 | 115 ms: 1.53x faster                                                 |
| float                    | 117 ms                                                 | 76.5 ms: 1.53x faster                                                |
| spectral_norm            | 170 ms                                                 | 111 ms: 1.53x faster                                                 |
| sqlglot_transpile        | 2.57 ms                                                | 1.69 ms: 1.53x faster                                                |
| pickle_pure_python       | 484 us                                                 | 318 us: 1.52x faster                                                 |
| logging_simple           | 8.30 us                                                | 5.48 us: 1.52x faster                                                |
| unpickle_pure_python     | 331 us                                                 | 219 us: 1.51x faster                                                 |
| logging_format           | 9.09 us                                                | 6.06 us: 1.50x faster                                                |
| hexiom                   | 10.4 ms                                                | 7.10 ms: 1.46x faster                                                |
| scimark_fft              | 466 ms                                                 | 320 ms: 1.46x faster                                                 |
| pprint_pformat           | 2.10 sec                                               | 1.45 sec: 1.45x faster                                               |
| pylint                   | 551 ms                                                 | 383 ms: 1.44x faster                                                 |
| pprint_safe_repr         | 1.02 sec                                               | 711 ms: 1.43x faster                                                 |
| django_template          | 48.2 ms                                                | 33.7 ms: 1.43x faster                                                |
| xml_etree_process        | 79.1 ms                                                | 56.0 ms: 1.41x faster                                                |
| fannkuch                 | 532 ms                                                 | 383 ms: 1.39x faster                                                 |
| thrift                   | 1.07 ms                                                | 795 us: 1.35x faster                                                 |
| regex_compile            | 188 ms                                                 | 141 ms: 1.34x faster                                                 |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.86 ms: 1.33x faster                                                |
| sqlalchemy_imperative    | 23.3 ms                                                | 17.6 ms: 1.32x faster                                                |
| html5lib                 | 88.9 ms                                                | 67.6 ms: 1.31x faster                                                |
| pycparser                | 1.58 sec                                               | 1.20 sec: 1.31x faster                                               |
| json_dumps               | 14.2 ms                                                | 10.9 ms: 1.31x faster                                                |
| genshi_text              | 31.8 ms                                                | 24.8 ms: 1.28x faster                                                |
| xml_etree_generate       | 99.4 ms                                                | 79.1 ms: 1.26x faster                                                |
| pathlib                  | 20.5 ms                                                | 16.3 ms: 1.25x faster                                                |
| dulwich_log              | 84.3 ms                                                | 68.2 ms: 1.24x faster                                                |
| 2to3                     | 348 ms                                                 | 282 ms: 1.24x faster                                                 |
| sqlglot_normalize        | 143 ms                                                 | 116 ms: 1.23x faster                                                 |
| nqueens                  | 106 ms                                                 | 88.7 ms: 1.19x faster                                                |
| json_loads               | 31.2 us                                                | 26.5 us: 1.18x faster                                                |
| sqlalchemy_declarative   | 172 ms                                                 | 148 ms: 1.17x faster                                                 |
| xml_etree_iterparse      | 115 ms                                                 | 101 ms: 1.15x faster                                                 |
| json                     | 5.69 ms                                                | 4.97 ms: 1.15x faster                                                |
| sqlglot_optimize         | 69.2 ms                                                | 60.5 ms: 1.14x faster                                                |
| sympy_str                | 346 ms                                                 | 304 ms: 1.14x faster                                                 |
| python_startup           | 14.6 ms                                                | 12.8 ms: 1.14x faster                                                |
| xml_etree_parse          | 168 ms                                                 | 148 ms: 1.13x faster                                                 |
| genshi_xml               | 66.0 ms                                                | 59.0 ms: 1.12x faster                                                |
| docutils                 | 3.30 sec                                               | 2.95 sec: 1.12x faster                                               |
| sympy_expand             | 566 ms                                                 | 506 ms: 1.12x faster                                                 |
| sympy_sum                | 196 ms                                                 | 176 ms: 1.12x faster                                                 |
| bench_thread_pool        | 986 us                                                 | 889 us: 1.11x faster                                                 |
| mdp                      | 2.85 sec                                               | 2.57 sec: 1.11x faster                                               |
| meteor_contest           | 120 ms                                                 | 108 ms: 1.10x faster                                                 |
| regex_v8                 | 27.8 ms                                                | 25.3 ms: 1.10x faster                                                |
| sympy_integrate          | 25.8 ms                                                | 23.6 ms: 1.09x faster                                                |
| sqlite_synth             | 3.02 us                                                | 2.79 us: 1.09x faster                                                |
| regex_dna                | 227 ms                                                 | 210 ms: 1.08x faster                                                 |
| pidigits                 | 191 ms                                                 | 186 ms: 1.02x faster                                                 |
| asyncio_websockets       | 559 ms                                                 | 552 ms: 1.01x faster                                                 |
| async_generators         | 444 ms                                                 | 458 ms: 1.03x slower                                                 |
| telco                    | 7.27 ms                                                | 7.64 ms: 1.05x slower                                                |
| coverage                 | 79.4 ms                                                | 84.3 ms: 1.06x slower                                                |
| python_startup_no_site   | 5.93 ms                                                | 7.13 ms: 1.20x slower                                                |
| gc_traversal             | 3.62 ms                                                | 4.73 ms: 1.30x slower                                                |
| create_gc_cycles         | 1.62 ms                                                | 2.70 ms: 1.67x slower                                                |
| bench_mp_pool            | 24.0 ms                                                | 85.2 ms: 3.55x slower                                                |
| Geometric mean           | (ref)                                                  | 1.36x faster                                                         |

Benchmark hidden because not significant (1): regex_effbot
Ignored benchmarks (15) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (11) of results/bm-20241115-3.14.0a1+-68dd6e6-JIT/bm-20241115-linux-x86_64-brandtbucher-justin_dwarf-3.14.0a1+-68dd6e6.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.389x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.29x
- 95% likely to have a speedup of 1.27x
- 99% likely to have a speedup of 1.23x

# Memory
- memory change: 1.37x