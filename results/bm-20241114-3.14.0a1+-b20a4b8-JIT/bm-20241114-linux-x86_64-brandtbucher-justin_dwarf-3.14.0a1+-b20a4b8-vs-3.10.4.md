# Results vs. 3.10.4

- fork: brandtbucher
- ref: justin_dwarf
- machine: linux-x86_64
- commit hash: b20a4b8
- commit date: 2024-11-14
- overall geometric mean: 1.192x faster
- HPT reliability: 99.99%
- HPT 99th percentile: 1.08x faster
- Memory change: 1.40x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241114-linux-x86_64-brandtbucher-justin_dwarf-3.14.0a1+-b20a4b8 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 1.29 sec: 3.70x slower                                               |
| docutils       | 3.30 sec                                               | 6.96 sec: 2.11x slower                                               |
| html5lib       | 88.9 ms                                                | 69.5 ms: 1.28x faster                                                |
| Geometric mean | (ref)                                                  | 1.83x slower                                                         |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241114-linux-x86_64-brandtbucher-justin_dwarf-3.14.0a1+-b20a4b8 |
|-------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| async_tree_none         | 728 ms                                                 | 339 ms: 2.15x faster                                                 |
| async_tree_memoization  | 870 ms                                                 | 422 ms: 2.06x faster                                                 |
| async_tree_io           | 1.77 sec                                               | 870 ms: 2.03x faster                                                 |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 579 ms: 1.76x faster                                                 |
| Geometric mean          | (ref)                                                  | 1.99x faster                                                         |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241114-linux-x86_64-brandtbucher-justin_dwarf-3.14.0a1+-b20a4b8 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 89.5 ms: 1.72x faster                                                |
| float          | 117 ms                                                 | 80.1 ms: 1.46x faster                                                |
| pidigits       | 191 ms                                                 | 187 ms: 1.02x faster                                                 |
| Geometric mean | (ref)                                                  | 1.37x faster                                                         |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241114-linux-x86_64-brandtbucher-justin_dwarf-3.14.0a1+-b20a4b8 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| regex_dna      | 227 ms                                                 | 214 ms: 1.06x faster                                                 |
| regex_compile  | 188 ms                                                 | 229 ms: 1.21x slower                                                 |
| regex_v8       | 27.8 ms                                                | 48.4 ms: 1.74x slower                                                |
| Geometric mean | (ref)                                                  | 1.19x slower                                                         |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241114-linux-x86_64-brandtbucher-justin_dwarf-3.14.0a1+-b20a4b8 |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| tomli_loads          | 3.14 sec                                               | 2.05 sec: 1.53x faster                                               |
| unpickle_pure_python | 331 us                                                 | 231 us: 1.43x faster                                                 |
| xml_etree_process    | 79.1 ms                                                | 60.4 ms: 1.31x faster                                                |
| xml_etree_generate   | 99.4 ms                                                | 83.1 ms: 1.20x faster                                                |
| xml_etree_parse      | 168 ms                                                 | 150 ms: 1.12x faster                                                 |
| xml_etree_iterparse  | 115 ms                                                 | 106 ms: 1.09x faster                                                 |
| json_loads           | 31.2 us                                                | 34.2 us: 1.09x slower                                                |
| pickle_pure_python   | 484 us                                                 | 628 us: 1.30x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.13x faster                                                         |

Benchmark hidden because not significant (1): json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241114-linux-x86_64-brandtbucher-justin_dwarf-3.14.0a1+-b20a4b8 |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 12.9 ms: 1.13x faster                                                |
| python_startup_no_site | 5.93 ms                                                | 7.16 ms: 1.21x slower                                                |
| Geometric mean         | (ref)                                                  | 1.03x slower                                                         |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241114-linux-x86_64-brandtbucher-justin_dwarf-3.14.0a1+-b20a4b8 |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| mako            | 16.3 ms                                                | 10.7 ms: 1.52x faster                                                |
| django_template | 48.2 ms                                                | 34.3 ms: 1.40x faster                                                |
| genshi_text     | 31.8 ms                                                | 26.2 ms: 1.22x faster                                                |
| genshi_xml      | 66.0 ms                                                | 60.6 ms: 1.09x faster                                                |
| Geometric mean  | (ref)                                                  | 1.30x faster                                                         |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241114-linux-x86_64-brandtbucher-justin_dwarf-3.14.0a1+-b20a4b8 |
|--------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 172 us: 3.17x faster                                                 |
| deltablue                | 7.91 ms                                                | 3.59 ms: 2.20x faster                                                |
| async_tree_none          | 728 ms                                                 | 339 ms: 2.15x faster                                                 |
| async_tree_memoization   | 870 ms                                                 | 422 ms: 2.06x faster                                                 |
| async_tree_io            | 1.77 sec                                               | 870 ms: 2.03x faster                                                 |
| generators               | 80.1 ms                                                | 39.7 ms: 2.02x faster                                                |
| richards_super           | 94.7 ms                                                | 47.7 ms: 1.99x faster                                                |
| richards                 | 79.3 ms                                                | 42.9 ms: 1.85x faster                                                |
| chaos                    | 115 ms                                                 | 62.6 ms: 1.84x faster                                                |
| deepcopy_memo            | 58.5 us                                                | 31.9 us: 1.83x faster                                                |
| crypto_pyaes             | 128 ms                                                 | 71.9 ms: 1.78x faster                                                |
| raytrace                 | 507 ms                                                 | 286 ms: 1.77x faster                                                 |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 579 ms: 1.76x faster                                                 |
| scimark_monte_carlo      | 118 ms                                                 | 67.9 ms: 1.74x faster                                                |
| scimark_sor              | 220 ms                                                 | 126 ms: 1.74x faster                                                 |
| nbody                    | 154 ms                                                 | 89.5 ms: 1.72x faster                                                |
| logging_silent           | 190 ns                                                 | 111 ns: 1.71x faster                                                 |
| go                       | 240 ms                                                 | 141 ms: 1.70x faster                                                 |
| deepcopy                 | 479 us                                                 | 284 us: 1.68x faster                                                 |
| djangocms                | 38.4 us                                                | 24.1 us: 1.60x faster                                                |
| sqlglot_parse            | 2.17 ms                                                | 1.36 ms: 1.60x faster                                                |
| tomli_loads              | 3.14 sec                                               | 2.05 sec: 1.53x faster                                               |
| comprehensions           | 28.8 us                                                | 18.8 us: 1.53x faster                                                |
| mako                     | 16.3 ms                                                | 10.7 ms: 1.52x faster                                                |
| coroutines               | 35.1 ms                                                | 23.1 ms: 1.52x faster                                                |
| scimark_lu               | 176 ms                                                 | 117 ms: 1.51x faster                                                 |
| sqlglot_transpile        | 2.57 ms                                                | 1.73 ms: 1.49x faster                                                |
| deepcopy_reduce          | 4.17 us                                                | 2.83 us: 1.47x faster                                                |
| float                    | 117 ms                                                 | 80.1 ms: 1.46x faster                                                |
| logging_format           | 9.09 us                                                | 6.31 us: 1.44x faster                                                |
| logging_simple           | 8.30 us                                                | 5.78 us: 1.44x faster                                                |
| unpickle_pure_python     | 331 us                                                 | 231 us: 1.43x faster                                                 |
| django_template          | 48.2 ms                                                | 34.3 ms: 1.40x faster                                                |
| spectral_norm            | 170 ms                                                 | 123 ms: 1.38x faster                                                 |
| scimark_fft              | 466 ms                                                 | 338 ms: 1.38x faster                                                 |
| hexiom                   | 10.4 ms                                                | 7.65 ms: 1.36x faster                                                |
| pprint_safe_repr         | 1.02 sec                                               | 763 ms: 1.33x faster                                                 |
| pprint_pformat           | 2.10 sec                                               | 1.58 sec: 1.33x faster                                               |
| pyflate                  | 716 ms                                                 | 543 ms: 1.32x faster                                                 |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.94 ms: 1.31x faster                                                |
| xml_etree_process        | 79.1 ms                                                | 60.4 ms: 1.31x faster                                                |
| fannkuch                 | 532 ms                                                 | 407 ms: 1.31x faster                                                 |
| sqlalchemy_imperative    | 23.3 ms                                                | 17.9 ms: 1.30x faster                                                |
| html5lib                 | 88.9 ms                                                | 69.5 ms: 1.28x faster                                                |
| pathlib                  | 20.5 ms                                                | 16.2 ms: 1.26x faster                                                |
| pycparser                | 1.58 sec                                               | 1.28 sec: 1.23x faster                                               |
| genshi_text              | 31.8 ms                                                | 26.2 ms: 1.22x faster                                                |
| xml_etree_generate       | 99.4 ms                                                | 83.1 ms: 1.20x faster                                                |
| nqueens                  | 106 ms                                                 | 91.1 ms: 1.16x faster                                                |
| python_startup           | 14.6 ms                                                | 12.9 ms: 1.13x faster                                                |
| xml_etree_parse          | 168 ms                                                 | 150 ms: 1.12x faster                                                 |
| genshi_xml               | 66.0 ms                                                | 60.6 ms: 1.09x faster                                                |
| bench_thread_pool        | 986 us                                                 | 906 us: 1.09x faster                                                 |
| xml_etree_iterparse      | 115 ms                                                 | 106 ms: 1.09x faster                                                 |
| mdp                      | 2.85 sec                                               | 2.65 sec: 1.07x faster                                               |
| meteor_contest           | 120 ms                                                 | 112 ms: 1.06x faster                                                 |
| regex_dna                | 227 ms                                                 | 214 ms: 1.06x faster                                                 |
| pidigits                 | 191 ms                                                 | 187 ms: 1.02x faster                                                 |
| asyncio_websockets       | 559 ms                                                 | 552 ms: 1.01x faster                                                 |
| sympy_integrate          | 25.8 ms                                                | 26.5 ms: 1.03x slower                                                |
| async_generators         | 444 ms                                                 | 464 ms: 1.05x slower                                                 |
| coverage                 | 79.4 ms                                                | 83.2 ms: 1.05x slower                                                |
| sympy_expand             | 566 ms                                                 | 601 ms: 1.06x slower                                                 |
| json_loads               | 31.2 us                                                | 34.2 us: 1.09x slower                                                |
| json                     | 5.69 ms                                                | 6.27 ms: 1.10x slower                                                |
| sqlite_synth             | 3.02 us                                                | 3.35 us: 1.11x slower                                                |
| dulwich_log              | 84.3 ms                                                | 97.0 ms: 1.15x slower                                                |
| python_startup_no_site   | 5.93 ms                                                | 7.16 ms: 1.21x slower                                                |
| regex_compile            | 188 ms                                                 | 229 ms: 1.21x slower                                                 |
| gc_traversal             | 3.62 ms                                                | 4.49 ms: 1.24x slower                                                |
| pickle_pure_python       | 484 us                                                 | 628 us: 1.30x slower                                                 |
| sympy_str                | 346 ms                                                 | 457 ms: 1.32x slower                                                 |
| sqlglot_normalize        | 143 ms                                                 | 197 ms: 1.38x slower                                                 |
| telco                    | 7.27 ms                                                | 10.5 ms: 1.44x slower                                                |
| sympy_sum                | 196 ms                                                 | 317 ms: 1.61x slower                                                 |
| sqlalchemy_declarative   | 172 ms                                                 | 283 ms: 1.65x slower                                                 |
| create_gc_cycles         | 1.62 ms                                                | 2.69 ms: 1.66x slower                                                |
| regex_v8                 | 27.8 ms                                                | 48.4 ms: 1.74x slower                                                |
| sqlglot_optimize         | 69.2 ms                                                | 142 ms: 2.05x slower                                                 |
| docutils                 | 3.30 sec                                               | 6.96 sec: 2.11x slower                                               |
| 2to3                     | 348 ms                                                 | 1.29 sec: 3.70x slower                                               |
| pylint                   | 551 ms                                                 | 2.05 sec: 3.73x slower                                               |
| bench_mp_pool            | 24.0 ms                                                | 108 ms: 4.50x slower                                                 |
| Geometric mean           | (ref)                                                  | 1.16x faster                                                         |

Benchmark hidden because not significant (3): json_dumps, regex_effbot, thrift
Ignored benchmarks (15) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (9) of results/bm-20241114-3.14.0a1+-b20a4b8-JIT/bm-20241114-linux-x86_64-brandtbucher-justin_dwarf-3.14.0a1+-b20a4b8.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, shortest_path, sphinx

- Geometric mean (including insignificant results): 1.192x faster
# HPT report

- Reliability score: 99.99% likely to be faster
- 90% likely to have a speedup of 1.16x
- 95% likely to have a speedup of 1.13x
- 99% likely to have a speedup of 1.08x

# Memory
- memory change: 1.40x