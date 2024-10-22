# Results vs. 3.10.4

- fork: brandtbucher
- ref: load_attr_property
- machine: linux-x86_64
- commit hash: 83e0a4e
- commit date: 2024-07-17
- overall geometric mean: 1.43x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.27x faster
- Memory change: 1.19x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240717-linux-x86_64-brandtbucher-load_attr_property-3.14.0a0-83e0a4e |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 270 ms: 1.29x faster                                                      |
| docutils       | 3.30 sec                                               | 2.87 sec: 1.15x faster                                                    |
| html5lib       | 88.9 ms                                                | 64.0 ms: 1.39x faster                                                     |
| tornado_http   | 136 ms                                                 | 92.5 ms: 1.47x faster                                                     |
| Geometric mean | (ref)                                                  | 1.32x faster                                                              |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240717-linux-x86_64-brandtbucher-load_attr_property-3.14.0a0-83e0a4e |
|-------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| async_tree_none         | 728 ms                                                 | 322 ms: 2.26x faster                                                      |
| async_tree_memoization  | 870 ms                                                 | 405 ms: 2.15x faster                                                      |
| async_tree_io           | 1.77 sec                                               | 842 ms: 2.10x faster                                                      |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 563 ms: 1.81x faster                                                      |
| Geometric mean          | (ref)                                                  | 2.07x faster                                                              |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240717-linux-x86_64-brandtbucher-load_attr_property-3.14.0a0-83e0a4e |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 80.7 ms: 1.90x faster                                                     |
| float          | 117 ms                                                 | 70.8 ms: 1.66x faster                                                     |
| pidigits       | 191 ms                                                 | 185 ms: 1.03x faster                                                      |
| Geometric mean | (ref)                                                  | 1.48x faster                                                              |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240717-linux-x86_64-brandtbucher-load_attr_property-3.14.0a0-83e0a4e |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 134 ms: 1.40x faster                                                      |
| regex_v8       | 27.8 ms                                                | 25.9 ms: 1.07x faster                                                     |
| regex_dna      | 227 ms                                                 | 221 ms: 1.02x faster                                                      |
| regex_effbot   | 3.63 ms                                                | 3.77 ms: 1.04x slower                                                     |
| Geometric mean | (ref)                                                  | 1.10x faster                                                              |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240717-linux-x86_64-brandtbucher-load_attr_property-3.14.0a0-83e0a4e |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| pickle_pure_python   | 484 us                                                 | 297 us: 1.63x faster                                                      |
| tomli_loads          | 3.14 sec                                               | 1.94 sec: 1.62x faster                                                    |
| unpickle_pure_python | 331 us                                                 | 215 us: 1.54x faster                                                      |
| xml_etree_process    | 79.1 ms                                                | 57.2 ms: 1.38x faster                                                     |
| json_dumps           | 14.2 ms                                                | 10.5 ms: 1.36x faster                                                     |
| xml_etree_generate   | 99.4 ms                                                | 80.9 ms: 1.23x faster                                                     |
| xml_etree_iterparse  | 115 ms                                                 | 99.1 ms: 1.17x faster                                                     |
| xml_etree_parse      | 168 ms                                                 | 147 ms: 1.14x faster                                                      |
| json_loads           | 31.2 us                                                | 27.7 us: 1.13x faster                                                     |
| Geometric mean       | (ref)                                                  | 1.34x faster                                                              |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240717-linux-x86_64-brandtbucher-load_attr_property-3.14.0a0-83e0a4e |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 10.5 ms: 1.38x faster                                                     |
| python_startup_no_site | 5.93 ms                                                | 7.15 ms: 1.20x slower                                                     |
| Geometric mean         | (ref)                                                  | 1.07x faster                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240717-linux-x86_64-brandtbucher-load_attr_property-3.14.0a0-83e0a4e |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| mako            | 16.3 ms                                                | 9.71 ms: 1.68x faster                                                     |
| django_template | 48.2 ms                                                | 35.2 ms: 1.37x faster                                                     |
| genshi_text     | 31.8 ms                                                | 24.7 ms: 1.29x faster                                                     |
| genshi_xml      | 66.0 ms                                                | 56.2 ms: 1.18x faster                                                     |
| Geometric mean  | (ref)                                                  | 1.37x faster                                                              |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240717-linux-x86_64-brandtbucher-load_attr_property-3.14.0a0-83e0a4e |
|--------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 166 us: 3.28x faster                                                      |
| generators               | 80.1 ms                                                | 29.2 ms: 2.74x faster                                                     |
| async_tree_none          | 728 ms                                                 | 322 ms: 2.26x faster                                                      |
| deltablue                | 7.91 ms                                                | 3.55 ms: 2.23x faster                                                     |
| async_tree_memoization   | 870 ms                                                 | 405 ms: 2.15x faster                                                      |
| async_tree_io            | 1.77 sec                                               | 842 ms: 2.10x faster                                                      |
| deepcopy_memo            | 58.5 us                                                | 28.7 us: 2.04x faster                                                     |
| richards_super           | 94.7 ms                                                | 47.4 ms: 2.00x faster                                                     |
| chaos                    | 115 ms                                                 | 58.0 ms: 1.99x faster                                                     |
| scimark_monte_carlo      | 118 ms                                                 | 60.6 ms: 1.95x faster                                                     |
| richards                 | 79.3 ms                                                | 41.0 ms: 1.93x faster                                                     |
| nbody                    | 154 ms                                                 | 80.7 ms: 1.90x faster                                                     |
| raytrace                 | 507 ms                                                 | 267 ms: 1.89x faster                                                      |
| crypto_pyaes             | 128 ms                                                 | 67.8 ms: 1.89x faster                                                     |
| asyncio_tcp              | 922 ms                                                 | 504 ms: 1.83x faster                                                      |
| logging_silent           | 190 ns                                                 | 105 ns: 1.81x faster                                                      |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 563 ms: 1.81x faster                                                      |
| deepcopy                 | 479 us                                                 | 272 us: 1.76x faster                                                      |
| scimark_sor              | 220 ms                                                 | 127 ms: 1.73x faster                                                      |
| comprehensions           | 28.8 us                                                | 16.7 us: 1.73x faster                                                     |
| sqlglot_parse            | 2.17 ms                                                | 1.27 ms: 1.71x faster                                                     |
| mako                     | 16.3 ms                                                | 9.71 ms: 1.68x faster                                                     |
| go                       | 240 ms                                                 | 144 ms: 1.67x faster                                                      |
| float                    | 117 ms                                                 | 70.8 ms: 1.66x faster                                                     |
| pylint                   | 551 ms                                                 | 335 ms: 1.65x faster                                                      |
| spectral_norm            | 170 ms                                                 | 104 ms: 1.63x faster                                                      |
| pickle_pure_python       | 484 us                                                 | 297 us: 1.63x faster                                                      |
| sqlglot_transpile        | 2.57 ms                                                | 1.58 ms: 1.62x faster                                                     |
| tomli_loads              | 3.14 sec                                               | 1.94 sec: 1.62x faster                                                    |
| pyflate                  | 716 ms                                                 | 442 ms: 1.62x faster                                                      |
| hexiom                   | 10.4 ms                                                | 6.58 ms: 1.58x faster                                                     |
| deepcopy_reduce          | 4.17 us                                                | 2.69 us: 1.55x faster                                                     |
| coroutines               | 35.1 ms                                                | 22.7 ms: 1.55x faster                                                     |
| unpickle_pure_python     | 331 us                                                 | 215 us: 1.54x faster                                                      |
| scimark_fft              | 466 ms                                                 | 307 ms: 1.52x faster                                                      |
| logging_simple           | 8.30 us                                                | 5.50 us: 1.51x faster                                                     |
| logging_format           | 9.09 us                                                | 6.06 us: 1.50x faster                                                     |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.37 ms: 1.48x faster                                                     |
| tornado_http             | 136 ms                                                 | 92.5 ms: 1.47x faster                                                     |
| fannkuch                 | 532 ms                                                 | 363 ms: 1.47x faster                                                      |
| pprint_safe_repr         | 1.02 sec                                               | 702 ms: 1.45x faster                                                      |
| pprint_pformat           | 2.10 sec                                               | 1.47 sec: 1.43x faster                                                    |
| scimark_lu               | 176 ms                                                 | 123 ms: 1.43x faster                                                      |
| asyncio_tcp_ssl          | 2.57 sec                                               | 1.81 sec: 1.42x faster                                                    |
| regex_compile            | 188 ms                                                 | 134 ms: 1.40x faster                                                      |
| html5lib                 | 88.9 ms                                                | 64.0 ms: 1.39x faster                                                     |
| python_startup           | 14.6 ms                                                | 10.5 ms: 1.38x faster                                                     |
| xml_etree_process        | 79.1 ms                                                | 57.2 ms: 1.38x faster                                                     |
| django_template          | 48.2 ms                                                | 35.2 ms: 1.37x faster                                                     |
| json_dumps               | 14.2 ms                                                | 10.5 ms: 1.36x faster                                                     |
| pycparser                | 1.58 sec                                               | 1.17 sec: 1.35x faster                                                    |
| thrift                   | 1.07 ms                                                | 800 us: 1.34x faster                                                      |
| genshi_text              | 31.8 ms                                                | 24.7 ms: 1.29x faster                                                     |
| 2to3                     | 348 ms                                                 | 270 ms: 1.29x faster                                                      |
| pathlib                  | 20.5 ms                                                | 15.9 ms: 1.29x faster                                                     |
| dulwich_log              | 84.3 ms                                                | 66.1 ms: 1.28x faster                                                     |
| sqlglot_normalize        | 143 ms                                                 | 112 ms: 1.27x faster                                                      |
| sqlglot_optimize         | 69.2 ms                                                | 55.6 ms: 1.24x faster                                                     |
| nqueens                  | 106 ms                                                 | 85.6 ms: 1.24x faster                                                     |
| xml_etree_generate       | 99.4 ms                                                | 80.9 ms: 1.23x faster                                                     |
| dask                     | 441 ms                                                 | 361 ms: 1.22x faster                                                      |
| bench_thread_pool        | 986 us                                                 | 831 us: 1.19x faster                                                      |
| sympy_sum                | 196 ms                                                 | 165 ms: 1.19x faster                                                      |
| sympy_str                | 346 ms                                                 | 292 ms: 1.18x faster                                                      |
| genshi_xml               | 66.0 ms                                                | 56.2 ms: 1.18x faster                                                     |
| xml_etree_iterparse      | 115 ms                                                 | 99.1 ms: 1.17x faster                                                     |
| sympy_integrate          | 25.8 ms                                                | 22.2 ms: 1.16x faster                                                     |
| docutils                 | 3.30 sec                                               | 2.87 sec: 1.15x faster                                                    |
| xml_etree_parse          | 168 ms                                                 | 147 ms: 1.14x faster                                                      |
| sympy_expand             | 566 ms                                                 | 494 ms: 1.14x faster                                                      |
| json_loads               | 31.2 us                                                | 27.7 us: 1.13x faster                                                     |
| json                     | 5.69 ms                                                | 5.07 ms: 1.12x faster                                                     |
| meteor_contest           | 120 ms                                                 | 107 ms: 1.12x faster                                                      |
| mdp                      | 2.85 sec                                               | 2.60 sec: 1.09x faster                                                    |
| regex_v8                 | 27.8 ms                                                | 25.9 ms: 1.07x faster                                                     |
| pidigits                 | 191 ms                                                 | 185 ms: 1.03x faster                                                      |
| regex_dna                | 227 ms                                                 | 221 ms: 1.02x faster                                                      |
| asyncio_websockets       | 559 ms                                                 | 555 ms: 1.01x faster                                                      |
| regex_effbot             | 3.63 ms                                                | 3.77 ms: 1.04x slower                                                     |
| async_generators         | 444 ms                                                 | 462 ms: 1.04x slower                                                      |
| gc_traversal             | 3.62 ms                                                | 3.88 ms: 1.07x slower                                                     |
| create_gc_cycles         | 1.62 ms                                                | 1.78 ms: 1.10x slower                                                     |
| telco                    | 7.27 ms                                                | 8.01 ms: 1.10x slower                                                     |
| coverage                 | 79.4 ms                                                | 94.9 ms: 1.19x slower                                                     |
| python_startup_no_site   | 5.93 ms                                                | 7.15 ms: 1.20x slower                                                     |
| Geometric mean           | (ref)                                                  | 1.43x faster                                                              |

Benchmark hidden because not significant (1): bench_mp_pool
Ignored benchmarks (15) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (5) of results/bm-20240717-3.14.0a0-83e0a4e-JIT/bm-20240717-linux-x86_64-brandtbucher-load_attr_property-3.14.0a0-83e0a4e.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.32x
- 95% likely to have a speedup of 1.31x
- 99% likely to have a speedup of 1.27x

# Memory
- memory change: 1.19x