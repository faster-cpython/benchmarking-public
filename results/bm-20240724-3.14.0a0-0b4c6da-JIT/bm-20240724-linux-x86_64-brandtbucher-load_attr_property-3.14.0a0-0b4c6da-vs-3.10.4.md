# Results vs. 3.10.4

- fork: brandtbucher
- ref: load_attr_property
- machine: linux-x86_64
- commit hash: 0b4c6da
- commit date: 2024-07-24
- overall geometric mean: 1.42x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.27x faster
- Memory change: 1.20x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240724-linux-x86_64-brandtbucher-load_attr_property-3.14.0a0-0b4c6da |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 271 ms: 1.29x faster                                                      |
| docutils       | 3.30 sec                                               | 2.90 sec: 1.14x faster                                                    |
| html5lib       | 88.9 ms                                                | 64.8 ms: 1.37x faster                                                     |
| tornado_http   | 136 ms                                                 | 92.9 ms: 1.47x faster                                                     |
| Geometric mean | (ref)                                                  | 1.31x faster                                                              |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240724-linux-x86_64-brandtbucher-load_attr_property-3.14.0a0-0b4c6da |
|-------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| async_tree_none         | 728 ms                                                 | 326 ms: 2.23x faster                                                      |
| async_tree_memoization  | 870 ms                                                 | 428 ms: 2.03x faster                                                      |
| async_tree_io           | 1.77 sec                                               | 905 ms: 1.95x faster                                                      |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 560 ms: 1.82x faster                                                      |
| Geometric mean          | (ref)                                                  | 2.00x faster                                                              |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240724-linux-x86_64-brandtbucher-load_attr_property-3.14.0a0-0b4c6da |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 81.0 ms: 1.89x faster                                                     |
| float          | 117 ms                                                 | 70.7 ms: 1.66x faster                                                     |
| pidigits       | 191 ms                                                 | 186 ms: 1.03x faster                                                      |
| Geometric mean | (ref)                                                  | 1.48x faster                                                              |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240724-linux-x86_64-brandtbucher-load_attr_property-3.14.0a0-0b4c6da |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 134 ms: 1.41x faster                                                      |
| regex_v8       | 27.8 ms                                                | 26.3 ms: 1.06x faster                                                     |
| regex_dna      | 227 ms                                                 | 230 ms: 1.01x slower                                                      |
| regex_effbot   | 3.63 ms                                                | 3.90 ms: 1.08x slower                                                     |
| Geometric mean | (ref)                                                  | 1.08x faster                                                              |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240724-linux-x86_64-brandtbucher-load_attr_property-3.14.0a0-0b4c6da |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| pickle_pure_python   | 484 us                                                 | 295 us: 1.64x faster                                                      |
| tomli_loads          | 3.14 sec                                               | 1.95 sec: 1.61x faster                                                    |
| unpickle_pure_python | 331 us                                                 | 217 us: 1.52x faster                                                      |
| xml_etree_process    | 79.1 ms                                                | 56.9 ms: 1.39x faster                                                     |
| json_dumps           | 14.2 ms                                                | 10.4 ms: 1.36x faster                                                     |
| xml_etree_generate   | 99.4 ms                                                | 80.6 ms: 1.23x faster                                                     |
| xml_etree_iterparse  | 115 ms                                                 | 98.6 ms: 1.17x faster                                                     |
| xml_etree_parse      | 168 ms                                                 | 148 ms: 1.14x faster                                                      |
| json_loads           | 31.2 us                                                | 28.3 us: 1.10x faster                                                     |
| Geometric mean       | (ref)                                                  | 1.34x faster                                                              |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240724-linux-x86_64-brandtbucher-load_attr_property-3.14.0a0-0b4c6da |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 10.6 ms: 1.38x faster                                                     |
| python_startup_no_site | 5.93 ms                                                | 7.17 ms: 1.21x slower                                                     |
| Geometric mean         | (ref)                                                  | 1.07x faster                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240724-linux-x86_64-brandtbucher-load_attr_property-3.14.0a0-0b4c6da |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| mako            | 16.3 ms                                                | 9.96 ms: 1.64x faster                                                     |
| django_template | 48.2 ms                                                | 35.9 ms: 1.34x faster                                                     |
| genshi_text     | 31.8 ms                                                | 24.5 ms: 1.30x faster                                                     |
| genshi_xml      | 66.0 ms                                                | 57.5 ms: 1.15x faster                                                     |
| Geometric mean  | (ref)                                                  | 1.35x faster                                                              |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240724-linux-x86_64-brandtbucher-load_attr_property-3.14.0a0-0b4c6da |
|--------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 171 us: 3.17x faster                                                      |
| generators               | 80.1 ms                                                | 28.3 ms: 2.83x faster                                                     |
| deltablue                | 7.91 ms                                                | 3.54 ms: 2.24x faster                                                     |
| async_tree_none          | 728 ms                                                 | 326 ms: 2.23x faster                                                      |
| deepcopy_memo            | 58.5 us                                                | 28.4 us: 2.06x faster                                                     |
| async_tree_memoization   | 870 ms                                                 | 428 ms: 2.03x faster                                                      |
| richards_super           | 94.7 ms                                                | 46.6 ms: 2.03x faster                                                     |
| richards                 | 79.3 ms                                                | 39.9 ms: 1.98x faster                                                     |
| chaos                    | 115 ms                                                 | 58.3 ms: 1.98x faster                                                     |
| scimark_monte_carlo      | 118 ms                                                 | 60.5 ms: 1.96x faster                                                     |
| async_tree_io            | 1.77 sec                                               | 905 ms: 1.95x faster                                                      |
| crypto_pyaes             | 128 ms                                                 | 66.6 ms: 1.92x faster                                                     |
| raytrace                 | 507 ms                                                 | 266 ms: 1.91x faster                                                      |
| nbody                    | 154 ms                                                 | 81.0 ms: 1.89x faster                                                     |
| logging_silent           | 190 ns                                                 | 102 ns: 1.86x faster                                                      |
| asyncio_tcp              | 922 ms                                                 | 504 ms: 1.83x faster                                                      |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 560 ms: 1.82x faster                                                      |
| comprehensions           | 28.8 us                                                | 16.4 us: 1.75x faster                                                     |
| deepcopy                 | 479 us                                                 | 274 us: 1.75x faster                                                      |
| scimark_sor              | 220 ms                                                 | 127 ms: 1.73x faster                                                      |
| sqlglot_parse            | 2.17 ms                                                | 1.26 ms: 1.72x faster                                                     |
| spectral_norm            | 170 ms                                                 | 101 ms: 1.69x faster                                                      |
| go                       | 240 ms                                                 | 144 ms: 1.67x faster                                                      |
| float                    | 117 ms                                                 | 70.7 ms: 1.66x faster                                                     |
| pickle_pure_python       | 484 us                                                 | 295 us: 1.64x faster                                                      |
| mako                     | 16.3 ms                                                | 9.96 ms: 1.64x faster                                                     |
| pyflate                  | 716 ms                                                 | 438 ms: 1.64x faster                                                      |
| sqlglot_transpile        | 2.57 ms                                                | 1.58 ms: 1.63x faster                                                     |
| tomli_loads              | 3.14 sec                                               | 1.95 sec: 1.61x faster                                                    |
| hexiom                   | 10.4 ms                                                | 6.55 ms: 1.59x faster                                                     |
| pylint                   | 551 ms                                                 | 348 ms: 1.58x faster                                                      |
| scimark_fft              | 466 ms                                                 | 305 ms: 1.53x faster                                                      |
| coroutines               | 35.1 ms                                                | 23.0 ms: 1.53x faster                                                     |
| unpickle_pure_python     | 331 us                                                 | 217 us: 1.52x faster                                                      |
| deepcopy_reduce          | 4.17 us                                                | 2.75 us: 1.52x faster                                                     |
| logging_simple           | 8.30 us                                                | 5.54 us: 1.50x faster                                                     |
| logging_format           | 9.09 us                                                | 6.08 us: 1.50x faster                                                     |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.35 ms: 1.49x faster                                                     |
| tornado_http             | 136 ms                                                 | 92.9 ms: 1.47x faster                                                     |
| pprint_safe_repr         | 1.02 sec                                               | 702 ms: 1.45x faster                                                      |
| pprint_pformat           | 2.10 sec                                               | 1.45 sec: 1.45x faster                                                    |
| asyncio_tcp_ssl          | 2.57 sec                                               | 1.80 sec: 1.42x faster                                                    |
| fannkuch                 | 532 ms                                                 | 374 ms: 1.42x faster                                                      |
| scimark_lu               | 176 ms                                                 | 125 ms: 1.41x faster                                                      |
| regex_compile            | 188 ms                                                 | 134 ms: 1.41x faster                                                      |
| xml_etree_process        | 79.1 ms                                                | 56.9 ms: 1.39x faster                                                     |
| python_startup           | 14.6 ms                                                | 10.6 ms: 1.38x faster                                                     |
| html5lib                 | 88.9 ms                                                | 64.8 ms: 1.37x faster                                                     |
| json_dumps               | 14.2 ms                                                | 10.4 ms: 1.36x faster                                                     |
| thrift                   | 1.07 ms                                                | 792 us: 1.35x faster                                                      |
| pycparser                | 1.58 sec                                               | 1.17 sec: 1.34x faster                                                    |
| django_template          | 48.2 ms                                                | 35.9 ms: 1.34x faster                                                     |
| genshi_text              | 31.8 ms                                                | 24.5 ms: 1.30x faster                                                     |
| 2to3                     | 348 ms                                                 | 271 ms: 1.29x faster                                                      |
| pathlib                  | 20.5 ms                                                | 16.0 ms: 1.28x faster                                                     |
| sqlglot_normalize        | 143 ms                                                 | 112 ms: 1.28x faster                                                      |
| dulwich_log              | 84.3 ms                                                | 67.7 ms: 1.25x faster                                                     |
| sqlglot_optimize         | 69.2 ms                                                | 56.0 ms: 1.24x faster                                                     |
| xml_etree_generate       | 99.4 ms                                                | 80.6 ms: 1.23x faster                                                     |
| dask                     | 441 ms                                                 | 362 ms: 1.22x faster                                                      |
| nqueens                  | 106 ms                                                 | 87.0 ms: 1.22x faster                                                     |
| bench_thread_pool        | 986 us                                                 | 825 us: 1.20x faster                                                      |
| sympy_str                | 346 ms                                                 | 293 ms: 1.18x faster                                                      |
| sympy_sum                | 196 ms                                                 | 167 ms: 1.17x faster                                                      |
| xml_etree_iterparse      | 115 ms                                                 | 98.6 ms: 1.17x faster                                                     |
| sympy_integrate          | 25.8 ms                                                | 22.1 ms: 1.17x faster                                                     |
| genshi_xml               | 66.0 ms                                                | 57.5 ms: 1.15x faster                                                     |
| xml_etree_parse          | 168 ms                                                 | 148 ms: 1.14x faster                                                      |
| docutils                 | 3.30 sec                                               | 2.90 sec: 1.14x faster                                                    |
| sympy_expand             | 566 ms                                                 | 498 ms: 1.14x faster                                                      |
| meteor_contest           | 120 ms                                                 | 106 ms: 1.13x faster                                                      |
| mdp                      | 2.85 sec                                               | 2.52 sec: 1.13x faster                                                    |
| json                     | 5.69 ms                                                | 5.15 ms: 1.10x faster                                                     |
| json_loads               | 31.2 us                                                | 28.3 us: 1.10x faster                                                     |
| regex_v8                 | 27.8 ms                                                | 26.3 ms: 1.06x faster                                                     |
| pidigits                 | 191 ms                                                 | 186 ms: 1.03x faster                                                      |
| regex_dna                | 227 ms                                                 | 230 ms: 1.01x slower                                                      |
| async_generators         | 444 ms                                                 | 450 ms: 1.01x slower                                                      |
| gc_traversal             | 3.62 ms                                                | 3.89 ms: 1.07x slower                                                     |
| regex_effbot             | 3.63 ms                                                | 3.90 ms: 1.08x slower                                                     |
| telco                    | 7.27 ms                                                | 7.89 ms: 1.09x slower                                                     |
| create_gc_cycles         | 1.62 ms                                                | 1.76 ms: 1.09x slower                                                     |
| coverage                 | 79.4 ms                                                | 92.3 ms: 1.16x slower                                                     |
| python_startup_no_site   | 5.93 ms                                                | 7.17 ms: 1.21x slower                                                     |
| Geometric mean           | (ref)                                                  | 1.42x faster                                                              |

Benchmark hidden because not significant (2): asyncio_websockets, bench_mp_pool
Ignored benchmarks (15) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (5) of results/bm-20240724-3.14.0a0-0b4c6da-JIT/bm-20240724-linux-x86_64-brandtbucher-load_attr_property-3.14.0a0-0b4c6da.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.32x
- 95% likely to have a speedup of 1.30x
- 99% likely to have a speedup of 1.27x

# Memory
- memory change: 1.20x